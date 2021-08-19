from django.http import request
from . import forms
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout


from . import models
# Create your views here.


class HomeView(generic.RedirectView):

	pattern_name = 'ex00:show-articles'
	def get(self, request, *args, **kwargs):
		# print(request.user)
		return super().get(request, *args, **kwargs)

class ShowArticlesView(generic.ListView):

	model = models.Article
	context_object_name='articles'
	template_name = 'ex00/show_articles.html'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['article_fields'] = [ field.name for field in models.Article._meta.fields ]
	# 	print(context)
	# 	return context

class ArticleDetailView(generic.DetailView):
	model = models.Article
	context_object_name='article'
	# slug_field = 'title'
	# default - MyModel.slug

class FavouriteArticlesView(generic.ListView):

	model = models.UserFavouriteArticle
	context_object_name='articles'
	template_name = 'ex00/favourite_articles.html'

	# queryset = models.UserFavouriteArticle.objects.filter(user=request.user) // cannot access to request
	def get_queryset(self):
		''' Returns the queryset that will be used to retrieve the object that this view will display. '''
		queryset = models.UserFavouriteArticle.objects.filter(user=self.request.user)
		return queryset

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	print(context)
	# 	return context

class LogInView(generic.FormView):

	template_name = 'ex00/login.html'
	form_class = forms.LogInForm
	success_url='/'

	def form_valid(self, form):
		user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
		login(self.request, user)
		return super(LogInView, self).form_valid(form)

class LogOutView(generic.RedirectView):

	http_method_names= [
		'get',
	]
	pattern_name='ex00:home'

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(LogOutView, self).get(request, *args, **kwargs)


class LikeView(generic.CreateView):	# with Model
	model = models.UserFavouriteArticle
	fields = [ 'user', 'article' ]
	success_url='/'

	def post(self, request, *args, **kwargs):
		print(request.POST['article'])
		return redirect('ex00:home')


class RegisterView(generic.CreateView): # with ModelForm
	form_class = forms.MyUserCreationForm
	success_url = '/'
	template_name = 'ex00/register.html'

	def form_valid(self, form):
		return super(RegisterView, self).form_valid(form)

	def form_invalid(self, form):
		return super(RegisterView, self).form_invalid(form)


class PublishView(generic.CreateView):
	form_class = forms.PublishForm
	success_url = '/'
	template_name = 'ex00/publish.html'

	def __init__(self, **kwargs) -> None:
		super(PublishView, self).__init__(**kwargs)

	def post(self, request, *args: str, **kwargs):
		print('POST CALLED')
		return super(PublishView, self).post(request, *args, **kwargs)

	def form_valid(self, form):
		print(self.get_form_class())
		print(type(form))
		print(form.cleaned_data)
		return super(PublishView, self).form_valid(form)

	def form_invalid(self, form):
		print(form.errors)
		return super(PublishView, self).form_invalid(form)



class AddFavouriteView(generic.CreateView):
	form_class = forms.AddFavouriteForm
	success_url = '/'
	template_name = 'ex00/add_favourite.html'

	def __init__(self, **kwargs):
		super(AddFavouriteView, self).__init__(**kwargs)

	def get_form_kwargs(self):
		kwargs = super(AddFavouriteView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		kwargs['article'] = self.request.POST['article']
		return kwargs

	def form_valid(self, form):
		print('valid')
		return super().form_valid(form)

	def form_invalid(self, form):
		print('invalid')
		return super().form_invalid(form)

	def post(self, request, *args: str, **kwargs):
		self.request.POST
		print('kwargs', kwargs)
		return super().post(request, *args, **kwargs)
