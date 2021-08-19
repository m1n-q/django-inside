from django import forms
from django.db.models import fields
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import HiddenInput
from . import models

class LogInForm(forms.Form):

	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)

	def clean(self):
		cleaned = super().clean()
		user = authenticate(username=cleaned['username'], password=cleaned['password'])
		# returns user object if atuhenticated
		if not user:
			raise ValidationError('Invalid Login')
		# print(cleaned)



class MyUserCreationForm(UserCreationForm): # Built-in ModelForm
	class Meta:
		model = models.User
		fields = ['username', 'password1', 'password2'] # UserCreationForm's fields


class PublishForm(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = '__all__'
		# widgets = {
		# 	'author' : forms.HiddenInput(attrs={'value':None}),
		# }
		# exclude = [
		# 	'author',
		# ]

		def __init__(self, user=None, *args, **kwargs ) -> None:
			super(PublishForm, self).__init__(*args, **kwargs)
			self.user = user

		def is_valid(self):
			print('IS_VALID METHOD CALLED')
			return super(PublishForm, self).is_valid()

		def clean(self):
			print('CLEAN METHOD CALLED')
			cleaned = super(PublishForm, self).clean()
			cleaned['author'] = self.user
			return cleaned


	# author = forms.HiddenInput()

class AddFavouriteForm(forms.ModelForm):
	class Meta:
		model = models.UserFavouriteArticle
		fields = ['article', 'user']
		widgets = {
			'article':HiddenInput,
			'user':HiddenInput,
		}


	def __init__(self, *args, **kwargs):
		super(AddFavouriteForm, self).__init__()
		self.fields['article'] = kwargs.pop('article',None)
		self.fields['user'] = kwargs.pop('user',None)
		print(kwargs.pop('article',None))
		print(kwargs.pop('user',None))



