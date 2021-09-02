from chat.views import room
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from .models import ChatRoom, User, Message
import json

# django의 기본 원리를 생각해보면 HTTP 요청을 받아들이고
# 매핑된 URL 로 이동, 이에 따라 views 에 함수를 실행합니다.
# 이와 유사하게 Channels역시 WebSocket 연결을 받아들이면,
# root routing configuration에서 소비자를 찾은 후에,
# 이벤트를 처리하기 위한 함수들을 호출합니다.

class ChatConsumer(AsyncWebsocketConsumer):

	@database_sync_to_async
	def get_user(self, username):
		try:
			return User.objects.get(username=username)
		except ObjectDoesNotExist:
			return None

	@database_sync_to_async
	def get_or_create_chatroom(self):
		try:
			return ChatRoom.objects.get(roomname=self.roomname)
		except ObjectDoesNotExist:
			newChatRoom = ChatRoom.objects.create(roomname=self.roomname)
			newChatRoom.save()
			print("New ChatRoom <%s> created!" % newChatRoom.roomname)
			return newChatRoom

	@database_sync_to_async
	def get_connected_users(self):
		return list(self.chatroom.user_set.all())

	@database_sync_to_async
	def add_user_to_chatroom(self):
		self.user.chatroom = self.chatroom
		self.user.save(update_fields=['chatroom'])

	@database_sync_to_async
	def del_user_from_chatroom(self):
		self.user.chatroom = None
		self.user.save(update_fields=['chatroom'])

	@database_sync_to_async
	def save_message(self, user, text, room):
		m = Message.objects.create(
			user=user,
			text=text,
			room=room
		)
		m.save()

	@database_sync_to_async
	def get_recent_messages(self):
		messages = self.chatroom.msg.all().order_by('when').reverse()[:3]
		messages = list(map(lambda x: (str(x.user), str(x.text)), messages))
		messages.reverse()
		return messages

	# obj.save() may have some side effects if you are not careful.
	# You retrieve the object with get(...) and all model field values are passed to your obj.
	# When you call obj.save(), django will save the current object state to record.
	# So if some changes happens between get() and save() by some other process,
	# then those changes will be lost.
	# use save(update_fields=[.....]) for avoiding such problems. // or update()

	async def connect(self):
		await self.accept()

		self.roomname = self.scope['url_route']['kwargs']['roomname']
		self.user = await self.get_user(self.scope['user'])
		self.chatroom = await self.get_or_create_chatroom()

		if self.user:
			await self.add_user_to_chatroom()

		await self.channel_layer.group_add(
			group=self.roomname,
			channel=self.channel_name
		)

		users = await self.get_connected_users()
		users = list(map(str, users))
		recent = await self.get_recent_messages()

		print(recent)
		await self.send(text_data=json.dumps({
			'recent':recent,
		}))

		await self.channel_layer.group_send(
			group=self.roomname,
			message={
				'type':'users',
				'users':users,
				'join':str(self.user),
			}
		)


	async def disconnect(self, close_code):
		if self.user:
			await self.del_user_from_chatroom()
		await self.channel_layer.group_discard(
			group=self.roomname,
			channel=self.channel_name
		)

		users = await self.get_connected_users()
		users = list(map(str, users))

		await self.channel_layer.group_send(
			group=self.roomname,
			message={
				'type':'users',
				'users':users,
				'left':str(self.user)
			}
		)

	async def receive(self, text_data):
		# text_data_json = json.loads(text_data)
		# message = text_data_json['message']
		# print(text_data)
		user, message = text_data.split(":", 1)
		await self.save_message(
			user=self.user,
			text=message,
			room=self.chatroom
		)
		await self.channel_layer.group_send(
			group=self.roomname,
			message={
				'type':'msg',
				'user':user,
				'message':message
			}
		)

	async def msg(self, event):
		# await self.send(text_data=user + ":" + message)
		await self.send(text_data=json.dumps({
			'user':event['user'],
			'message':event['message']
		}))

	async def users(self, event):
		users = event['users']
		if 'join' in event:
			await self.send(text_data=json.dumps({
				'users':users,
				'join':event['join'],
			}))
		elif 'left' in event:
			await self.send(text_data=json.dumps({
				'users':users,
				'left':event['left']
			}))
