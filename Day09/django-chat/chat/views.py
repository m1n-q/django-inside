from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView

def mainpage(request):
	return render(request, 'chat/mainpage.html')

def room(request, roomname):
	print(roomname)
	return render(request, 'chat/room.html', {'roomname':roomname})

def room1(request):
	return render(request, 'chat/room.html', {'roomname':'room1'})

def room2(request):
	return render(request, 'chat/room.html', {'roomname':'room2'})

def room3(request):
	return render(request, 'chat/room.html')

