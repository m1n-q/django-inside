from django.urls import path
from . import views

app_name = 'ex01'
urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('articles/', views.ShowArticlesView.as_view(), name='show-articles'),
	path('detail/<str:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
	path('favourites/', views.FavouriteArticlesView.as_view(), name='favourite-articles'),
	path('login/', views.LogInView.as_view(), name='login'),
	path('logout/', views.LogOutView.as_view(), name='logout'),
	path('register/', views.RegisterView.as_view(), name='register'),
	path('publish/', views.PublishView.as_view(), name='publish'),
	path('add_favourite/', views.AddFavouriteView.as_view(), name='add-favourite'),
	path('del_favourite/<int:pk>', views.DelFavouriteView.as_view(), name='del-favourite'),
]

