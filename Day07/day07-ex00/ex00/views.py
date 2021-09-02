from . import forms
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.utils.text import slugify
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

class ArticleDetailView(generic.edit.FormMixin, generic.DetailView):
	model = models.Article
	context_object_name='article'
	form_class = forms.AddFavouriteForm
	# slug_field = 'title'
	# default - MyModel.slug

	# 다른 view로 post 했음. post 할때 이미 모델을 만들어서 보내나...?
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			try:
				context['is_user_favourite'] = models.UserFavouriteArticle.objects.get(user=self.request.user, article=context['article'])
			except models.UserFavouriteArticle.DoesNotExist:
				context['is_user_favourite'] = None
		return context

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['user_id'] = self.request.user.id
		kwargs['article_id'] = self.object.id
		return kwargs


class FavouriteArticlesView(generic.ListView):

	model = models.UserFavouriteArticle
	context_object_name='articles'
	template_name = 'ex00/favourite_articles.html'

	# queryset = models.UserFavouriteArticle.objects.filter(user=request.user) // cannot access to request
	def get_queryset(self):
		''' Returns the queryset that will be used to retrieve the object that this view will display. '''
		if self.request.user.is_authenticated:
			queryset = models.UserFavouriteArticle.objects.filter(user=self.request.user)
		else:
			queryset = None
		return queryset


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


class RegisterView(generic.CreateView): # with ModelForm
	model = models.User
	form_class = forms.MyUserCreationForm
	success_url = '/'
	template_name = 'ex00/register.html'

	def form_valid(self, form):
		return super(RegisterView, self).form_valid(form)

	def form_invalid(self, form):
		return super(RegisterView, self).form_invalid(form)


class PublishView(generic.CreateView):
	model = models.Article
	form_class = forms.PublishForm
	template_name = 'ex00/publish.html'

	def get_success_url(self):
		return '/detail/' + self.object.slug

	def get_form_kwargs(self):
		kwargs = super(PublishView, self).get_form_kwargs()
		kwargs['user_id'] = self.request.user.id
		return kwargs

	def post(self, request, *args: str, **kwargs):
		return super(PublishView, self).post(request, *args, **kwargs)


class AddFavouriteView(generic.CreateView):
	# action to this url work. is it ok?!
	# path('add_favourite/', views.AddFavouriteView.as_view(), name='add-favourite'),

	model = models.UserFavouriteArticle
	fields = ['article', 'user']


	template_name = 'ex00/add_favourite.html'

	# kwargs['data'] == request.POST 로 들어온애들.

	# model_choice_field :  기본적으로는 instance 로 바로 선택할 수 있는게 아니라,
	# 						id 를 value 로 하여 제출받고, id 에 맞는 model instance 로 변환하는듯.

	def get_success_url(self):
		return self.request.META.get('HTTP_REFERER')

	def form_valid(self, form):
		if self.request.user.is_authenticated:
			return super(AddFavouriteView, self).form_valid(form)
		else:
			return redirect('/detail/' + form.instance.article.slug)

	def form_invalid(self, form):
		# if only article and no user:
		# <default flow in Form>
		# is_bound : O
		# cleaned_data['article'] and error['user'] have been made in clean()
		# is_valid (is_bound & no errors): X
		#
		# <to ModelForm>
		# construct instance from cleaned_data
		# so, make instance with only 'article' field
		article = form.instance.article
		slug = article.slug
		return redirect('/detail/' + slug)




class DelFavouriteView(generic.DeleteView):
	model = models.UserFavouriteArticle


	def get_success_url(self) -> str:
		return self.request.META.get('HTTP_REFERER')

	def post(self, request, *args: str, **kwargs):
		print('DEL', self.request.POST)	#input 태그 이름은 상관없구낭...
		print('DEL', self.request.META.get('HTTP_REFERER'))
		return super().post(request, *args, **kwargs)


