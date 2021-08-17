from django import forms
from .models import Movies







class TitleDropDownForm(forms.Form):
	title = forms.ModelChoiceField(queryset=Movies.objects.all(), empty_label=None)

	# with all() :
	# to_field_name='...'	: values, default=pk
	# text : __str__

	# with only(), it will get a instance that has only one column.

	opening_crawl = forms.CharField(widget=forms.Textarea)
