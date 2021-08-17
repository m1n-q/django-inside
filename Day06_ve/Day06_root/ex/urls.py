from django.urls import path
from . import views

app_name='ex'
urlpatterns = [
	path('', views.home),
	path('signup/', views.signup),
	path('signin/', views.signin),
	path('out/', views.out),
	path('vote/', views.vote, name='vote'),
	path('delpost/', views.delpost, name='delpost'),
	path('addpost/', views.addpost, name='addpost'),
]
