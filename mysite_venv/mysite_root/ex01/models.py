from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.text import slugify
import os, shutil
from mysite.settings import MEDIA_ROOT


class User(AbstractUser):
	def path_file_name(instance, filename):
		return os.path.join(instance.username, filename)
	chatroom = models.ForeignKey(to='chat.ChatRoom', on_delete=SET_NULL, null=True)
	intro = models.CharField(max_length=20, default="Hello, World!")
	profimg = models.ImageField(upload_to=path_file_name, blank=True, default=None)

	def save(self, *args, **kwargs):
		if not self.profimg:
			self.profimg = self.username + '/prof.jpg'
			os.mkdir(MEDIA_ROOT / self.username)
			shutil.copyfile(src = MEDIA_ROOT / 'prof.jpg',  dst = MEDIA_ROOT / str(self.profimg))
		return super().save(*args, **kwargs)




class Article(models.Model):
	title = models.CharField(max_length=64, null=False)
	author = models.ForeignKey(to=User, on_delete=CASCADE, null=False) 	# many to one
	created = models.DateTimeField(auto_now_add=True, null=False)
	synopsis = models.CharField(max_length=312, null=False)
	content = models.TextField(null=False)
	slug = models.SlugField(allow_unicode=True, null=True)

	def save(self, *args, **kargs):
		if not self.slug:
			self.slug = slugify(self.title, allow_unicode=True)
		return super(Article, self).save(*args, **kargs)

	def __str__(self):
		return self.title

class UserFavouriteArticle(models.Model):
	# 한 테이블에 같은 유저 여러개 있을 수 있음.
	# record : USER / ARTICLE 형태!
	# Many to one : 한 user, 한 3article 에 대해 Favourite articles 이 여러개 있을 수 있음

	user = models.ForeignKey(to=User, on_delete=CASCADE, null=False) # many to one
	article = models.ForeignKey(to=Article, on_delete=CASCADE, null=False) # many to one
	# User class 에 many to many field 로 설정한것과 같다!

	# related_name= 역참조시 (reference 받는 쪽에서 참조시) 이름?




	# user = models.ManyToManyField(to=User, related_name='user')
	# article = models.ManyToManyField(to=Article,related_name='article')

	def __str__(self):
		return self.article.title
