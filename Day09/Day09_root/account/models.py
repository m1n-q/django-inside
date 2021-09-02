from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL


class User(AbstractUser):
	chatroom = models.ForeignKey(to='chat.ChatRoom', on_delete=SET_NULL, null=True)

# Create your models here.
