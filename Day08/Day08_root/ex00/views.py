from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import TitleImg
from django.forms import TextInput

# Create your views here.

class AddImgView(CreateView):
	model = TitleImg
	fields = '__all__'
	template_name = 'ex00/add-img.html'

	def get_success_url(self):
		return '/'

	def get_form(self):
		form = super().get_form()
		form.fields['title'].widget = TextInput()
		return form


class ShowImgsView(ListView):
	model = TitleImg
	template_name = 'ex00/show-imgs.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


