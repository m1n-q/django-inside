from django.shortcuts import render
from django.views.generic import CreateView
from .models import TitleImg
from PIL import Image

# Create your views here.

class AddImgView(CreateView):
	model = TitleImg
	fields = '__all__'
	template_name = 'ex00/add-img.html'

	def get_success_url(self):
		image = Image.open(self.object.img)
		image.show()


		return '/ex00/add-img/'




# class AddImgSuccessView(View):
