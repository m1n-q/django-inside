from django import forms
from django.forms import fields
from .models import TitleImg

class AddTitleForm(forms.ModelForm):
	class Meta:
		model = TitleImg
		fields = '__all__'

