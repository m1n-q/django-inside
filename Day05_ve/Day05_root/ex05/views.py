from django.db.models import fields
from django.forms.models import ModelChoiceField
from django.shortcuts import get_object_or_404, render, redirect
from .models import Movies
from datetime import date
from .forms import TitleDropDownForm

data = [
    {'epi_nb': 1, 'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'rel_date': date(1999, 5, 19)},
    {'epi_nb': 2, 'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'rel_date': date(2002, 5, 16)},
    {'epi_nb': 3, 'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'rel_date': date(2005, 5, 19)},
    {'epi_nb': 4, 'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'rel_date': date(1977, 5, 25)},
    {'epi_nb': 5, 'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kurtz, Rick McCallum', 'rel_date': date(1980, 5, 17)},
    {'epi_nb': 6, 'title': 'Return of the Jedi', 'director': 'Richard Marquand', 'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum', 'rel_date': date(1983, 5, 25)},
    {'epi_nb': 7, 'title': 'The Force Awakens', 'director': 'J. J. Abrams', 'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'rel_date': date(2015, 12, 11)},
]

def populate(request):
	errors = []
	for d in data:
		try:
			Movies.objects.create(
				episode_nb=d['epi_nb'],
				title=d['title'],
				director=d['director'],
				producer=d['producer'],
				release_date=d['rel_date']
			)
		except Exception as e:
			errors.append(str(e))
	print(errors)
	if not errors:
		return render(request, 'ex05/populate.html')
	else:
		return render(request, 'ex05/populate.html', {'errors' : errors})

def display(request):
	errors = []
	movies = Movies.objects.all()
	if not movies:
		return render(request, 'ex05/display.html', {'msg': 'No available data.'})

	records = Movies.objects.values_list()
	return render(request, 'ex05/display.html', {'records' : records})


def remove(request):
	msg = ''
	if request.method == 'POST':
		form = TitleDropDownForm(request.POST)
		if form.is_valid():
			form.cleaned_data['title'].delete()
		return redirect(request.META.get('HTTP_REFERER'))
	else:
		form = TitleDropDownForm()
	if not form.fields['title'].queryset:
		msg = 'No data available.'

	# msg = "No data available."
	return render(request, 'ex05/remove.html', context={'form' : form, 'msg' : msg})




