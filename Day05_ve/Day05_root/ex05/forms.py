from django import forms
from django.forms.models import ModelChoiceField
from .models import Movies







class TitleDropDownForm(forms.Form):
	title = ModelChoiceField(queryset=Movies.objects.only('title'), empty_label=None)
