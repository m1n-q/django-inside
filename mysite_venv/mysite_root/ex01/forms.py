from django import forms

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
		widgets = {
			'author' : forms.HiddenInput,
			'slug' : forms.HiddenInput,
		}


	def __init__(self, *args, **kwargs):
		user_id = kwargs.pop('user_id', None)
		super(PublishForm, self).__init__(*args, **kwargs)
		self.fields['author'].initial = models.User.objects.get(id=user_id)
		self.fields['slug'].required = False
		self.fields['slug'].initial = None

class AddFavouriteForm(forms.ModelForm):

	class Meta:
		model = models.UserFavouriteArticle
		fields = ['article', 'user']
		widgets = {
			'article':HiddenInput,
			'user':HiddenInput,
		}

	def __init__(self, *args, **kwargs):
		article_id = kwargs.pop('article_id',None)
		user_id = kwargs.pop('user_id', None)
		super(AddFavouriteForm, self).__init__(*args, **kwargs)
		self.fields['article'].initial = models.Article.objects.get(id=article_id)
		try:
			self.fields['user'].initial = models.User.objects.get(id=user_id)
		except models.User.DoesNotExist:
			self.fields['user'].initial = None
