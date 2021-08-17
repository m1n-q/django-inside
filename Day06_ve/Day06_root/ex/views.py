
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission

from . import forms, models
import random
import datetime

# how could I get session info here ?
# why session in request, instead of response?
# 이미 들어온 request 에 대해 처리한건데, 다시 들어온 request에서 어떻게 알지?
# 리퀘스트.세션으로 사용하는 이유는, 리퀘스트의 쿠키의 있는 id를 가져와서, db의 해당 세션아이디를 찾아서, 그곳의 데이터를 꺼내는 것입니까?




def delpost(request):
	tip = models.Tip.objects.get(id=request.POST['tip_id'])
	# print(request.POST)
	# tip.delete()
	if tip.author == request.user or request.user.has_perm('ex.delete_tip'):
		tip.delete()
	else:
		raise PermissionDenied
	return redirect('/')


def vote(request):

	tip = models.Tip.objects.get(id=request.POST['tip_id'])
	# print(tip.like.all())
	if 'like' in request.POST:
		if request.user in tip.like.all():
			tip.like.remove(request.user)
		elif request.user in tip.dislike.all():
			tip.dislike.remove(request.user)
		else:
			tip.like.add(request.user)


	elif 'dislike' in request.POST:
		if tip.author == request.user or request.user.has_perm('ex.downvote_tip'):
			if request.user in tip.dislike.all():
				tip.dislike.remove(request.user)
			elif request.user in tip.like.all():
				tip.like.remove(request.user)
			else:
				tip.dislike.add(request.user)
		else:
			raise PermissionDenied



	return redirect('/')


@permission_required('ex.add_tip', login_url='/signin/')
def addpost(request):

	tipform = forms.TipForm(request.POST)
	if tipform.is_valid():
		models.Tip.objects.create(
			content=tipform.cleaned_data['content'],
			author=request.user,
			date=datetime.date.today()
		)
	return redirect('/')


def home(request):

	signed = False
	tipform = None
	reputation = 'Anonymous'

	if request.user.is_authenticated:
		signed = True
		request.session['username'] = str(request.user)
		request.session.set_expiry(0)
		tipform = forms.TipForm()
		reputation = request.user.reputation

	else: # anonymous
		cur = request.session.get('username', None)
		if cur:
			pass
		else:
			anon = random.choice(settings.SESSION_NAMES)
			request.session['username'] = anon
			request.session.set_expiry(42)

	tips = models.Tip.objects.all()
	res = render(
		request,
		'ex/home.html',
		context={
			'username': request.session['username'],
			'signed':signed,
			'tips':tips,
			'tipform':tipform,
			'reputation':reputation
		}
	)
	return res


def signup(request):
	if request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = models.User.objects.create_user(username=data['username'], password=data['password'])
			addperm = Permission.objects.get(codename='add_tip')
			viewperm = Permission.objects.get(codename='view_tip')
			user.user_permissions.set([addperm, viewperm])
			user.save()	# user object

			# skip authenticate (already we had user object)
			login(request, user)
			return redirect('/')
	else:
		form = forms.SignUpForm()

	# password input 은 binding 되어도 auto-filling 안되는듯!
	return render(request, 'ex/signup.html', {'form':form})


# Use authenticate() to verify a set of credentials.
# It takes credentials as keyword arguments, username and password for the default case,
# checks them against each authentication backend,
# and returns a <User object>
# if the credentials are valid for a backend.
# If the credentials aren’t valid for any backend or if a backend raises PermissionDenied,
# it returns None.

def signin(request):
	if request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		form = forms.SignInForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(request, username=data['username'], password=data['password'])
			login(request, user)
			return redirect('/')

	else:
		form = forms.SignInForm()

	return render(request, 'ex/signin.html', {'form':form})

def out(request):
	logout(request)
	return redirect('/')
