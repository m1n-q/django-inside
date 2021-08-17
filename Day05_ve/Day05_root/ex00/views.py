from django.shortcuts import render
from . import psy

def init(request):
	psy.create_movies_table()
	return render(request, 'ex00/init.html')
