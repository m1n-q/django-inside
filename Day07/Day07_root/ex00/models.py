from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils.text import slugify

class User(AbstractUser):
	# userfavouritearticle = models.ManyToManyField(to='Article', related_name='userfavouritearticle', related_query_name='userfavouritearticle')
	pass

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




	# user = models.ManyToManyField(to=User, related_name='user')
	# article = models.ManyToManyField(to=Article,related_name='article')

	def __str__(self):
		return self.article.title
