from django.urls import path

from . import views

app_name='ex01'
urlpatterns = [
	path('django/', views.ex01_index, name='django_index'),
	path('display', views.ex01_display, name='django_display'),
	path('templates', views.ex01_templates, name='django_templates'),
]
