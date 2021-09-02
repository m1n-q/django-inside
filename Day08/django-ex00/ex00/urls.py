from django.urls import path
from . import views

app_name='ex00'
urlpatterns=[
	path('add-img/', views.AddImgView.as_view(), name='add-img')
]
