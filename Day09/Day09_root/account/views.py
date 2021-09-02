from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_POST
from .models import User



def mainpage(request):
	form = AuthenticationForm
	return render(request, 'account/mainpage.html', {'form':form})

@require_POST
def signin(request):
	form = AuthenticationForm(request, data=request.POST)
	if form.is_valid():
		# username = form.cleaned_data['username']
		# password = form.cleaned_data['password']
		# user = authenticate
		print('VALID')
		print(request.POST)
		user = form.get_user()
		login(request, user)
	else:
		user = None
		print('INVALID')
		print(form.errors)
	return JsonResponse(data={'username':user.username})

def signout(request):
	print('SIGN OUT', request.POST)
	logout(request)
	return JsonResponse(data={'username':request.user.username})

class SignUpView(generic.CreateView):
	template_name='account/signup.html'
	success_url='/'
	def get_form_class(self):
		class MyUserCreationForm(UserCreationForm):
			class Meta:
				model=User
				fields = ['username', 'password1', 'password2']
		return MyUserCreationForm
