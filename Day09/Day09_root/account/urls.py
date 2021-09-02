from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
	path('', views.mainpage, name='mainpage'),
	# path('login/', views.LogInView.as_view(), name='login'),
	path('signin/', views.signin, name='signin'),
	path('signout/', views.signout, name='signout'),
	path('signup/', views.SignUpView.as_view(), name='signup'),
]
