from django.db import models

# Create your models here.
class TitleImg(models.Model):
	title = models.TextField(unique=True, null=False)
	img = models.ImageField(upload_to='photo/%Y/%m/%d', null=False)
