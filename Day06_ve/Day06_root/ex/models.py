
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_delete, post_init


# Create your models here.




class Tip(models.Model):
	class Meta:
		permissions = [
			("downvote_tip", "Can down vote tip"),
		]
	content = models.TextField()
	author = models.ForeignKey('User', on_delete=CASCADE)	# many to one
	date = models.DateField()
	like = models.ManyToManyField(to='User', related_name='like_users')
	dislike = models.ManyToManyField(to='User', related_name='dislike_users')

class User(AbstractUser):
	reputation = models.IntegerField(default=0)

	@receiver(m2m_changed, sender=Tip.like.through)
	@receiver(m2m_changed, sender=Tip.dislike.through)
	@receiver(post_delete, sender=Tip)
	def set_reputation(sender, **kwargs):
		user = kwargs['instance'].author
		sig = kwargs.get('action', None)
		if sig == 'post_add' or sig == 'post_remove' or not sig:
			total = 0
			tips = Tip.objects.filter(author=user)
			for tip in tips:
				total += tip.like.count() * 5
				total -= tip.dislike.count() * 2
			user.reputation = total
			user.set_permissions()
			user.save()


	def set_permissions(self):
		delperm = Permission.objects.get(codename='delete_tip')
		downperm = Permission.objects.get(codename='downvote_tip')
		if self.reputation >= 30 and not self.has_perm(delperm):
			self.user_permissions.add(delperm)
		elif self.reputation >= 15 and not self.has_perm(downperm):
			self.user_permissions.add(downperm)
