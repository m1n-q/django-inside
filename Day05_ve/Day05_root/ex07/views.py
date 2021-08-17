from django.db.models import fields
from django.forms.models import ModelChoiceField
from django.http.request import RawPostDataException
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
	if not errors:
		return render(request, 'ex07/populate.html')
	else:
		return render(request, 'ex07/populate.html', {'errors' : errors})

def display(request):
	errors = []
	movies = Movies.objects.all()
	col_names = list(map(lambda x: str(x).split('.')[-1].capitalize(), Movies._meta.get_fields()))
	if not movies:
		return render(request, 'ex07/display.html', {'msg': 'No available data.'})

	records = Movies.objects.values_list()
	return render(request, 'ex07/display.html', {'records' : records, 'col_names': col_names})


def update(request):
	msg = ''
	if request.method == 'POST':
		form = TitleDropDownForm(request.POST)
		if form.is_valid():

			#method 1
			movie = form.cleaned_data['title']
			movie.opening_crawl = form.cleaned_data['opening_crawl']
			movie.save()
			# if with objects.only(), it will updates opening_crawl properly, but not updated_time
			# 1) movie.updated
			# 2) movie.save(update_fields=['opening_crawl', 'updated'])
			# 3) use all() instead. ( it is not displaying all columns. getting instance with all coulmns, and just displaying __str__ )

		#method 2
		# h = Movies.objects.get(pk=1)
		# h.opening_crawl = 'HAND WRITTEN MESSAGE!'
		# h.save()


		return redirect(request.META.get('HTTP_REFERER'))
	else:
		form = TitleDropDownForm()
	if not form.fields['title'].queryset:
		msg = 'No data available.'

	return render(request, 'ex07/update.html', context={'form' : form, 'msg' : msg})




