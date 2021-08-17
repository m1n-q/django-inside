from ex09.models import People, Planets
from django.shortcuts import render

# Create your views here.


def display(request):
	pp = People.objects.filter(homeworld__climate__contains='windy').order_by('name').all()

	if len(pp) == 0:
		pp = ''

	return render(request, 'ex09/display.html', context={'people' : pp})
