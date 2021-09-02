from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
	path('', views.mainpage, name='mainpage'),
	path('<str:roomname>/', views.room, name='room'),

	# send <route argument> to view as keyword argument

	# path('room1/', views.room1, name='room1'),
	# path('room2/', views.room2, name='room2'),
	# path('room3/', views.room3, name='room3'),
]
