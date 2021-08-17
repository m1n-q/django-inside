from . import models
from django import forms

class SearchingForm(forms.Form):
	choices = [ (gender[0], gender[0]) for gender in models.People.objects.values_list('gender').distinct()]


	rel_date_min = forms.DateField()
	rel_date_max = forms.DateField()
	diameter = forms.IntegerField()
	gender = forms.ChoiceField(choices=choices)
