from django.db import models
from account.models import User

# Create your models here.
class ChatRoom(models.Model):
	roomname = models.CharField(max_length=20, unique=True)


class Message(models.Model):
	text = models.TextField(max_length=200)
	when = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
	room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE, related_name='msg')

# CASCADE : row 자체가 함께 삭제됨
# SET_NULL : 해당 필드만 NULL
