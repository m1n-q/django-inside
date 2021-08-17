from django.db import models

# Create your models here.
class Movies(models.Model):
	'''
		• title: unique, variable character chain, 64 byte maximum size, non null.
		• episode_nb: integer, PRIMARY KEY.
		• opening_crawl: text, can be null, no size limit.
		• director: variable character chain, non null, 32 bytes maximum size.
		• producer: variable character chain, non null, 128 bytes maximum size.
		• release_date: date (without time), non null.
	'''
	episode_nb = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=64, unique=True, null=False)	#null : default True
	opening_crawl = models.TextField(null=True)
	director = models.CharField(max_length=32)
	producer = models.CharField(max_length=128)
	release_date = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, editable=True)

	def __str__(self):
		return self.title
