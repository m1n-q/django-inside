from django.urls import path
from . import consumers

websocket_urlpatterns = [
	path('ws/chat/<str:roomname>/', consumers.ChatConsumer.as_asgi()),
	# pattern will be sended to consumer.scope['url_route']
]

# django의 url 과 유사합니다.
# 이 routing 파일을 django가 인식할 수 있도록 추가해줘야합니다.


# We call the as_asgi() classmethod in order to
# get an ASGI application that
# will instantiate an instance of our consumer for each user-connection.
# This is similar to Django’s as_view(),
# which plays the same role for per-request Django view instances.
