from django.shortcuts import redirect, render
from . import psy, forms
from datetime import date


data = [
    {'epi_nb': 1, 'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'rel_date': date(1999, 5, 19)},
    {'epi_nb': 2, 'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'rel_date': date(2002, 5, 16)},
    {'epi_nb': 3, 'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'rel_date': date(2005, 5, 19)},
    {'epi_nb': 4, 'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'rel_date': date(1977, 5, 25)},
    {'epi_nb': 5, 'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kurtz, Rick McCallum', 'rel_date': date(1980, 5, 17)},
    {'epi_nb': 6, 'title': 'Return of the Jedi', 'director': 'Richard Marquand', 'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum', 'rel_date': date(1983, 5, 25)},
    {'epi_nb': 7, 'title': 'The Force Awakens', 'director': 'J. J. Abrams', 'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'rel_date': date(2015, 12, 11)},
]

# Create your views here.
def init(request):
	msg = psy.create_movies_table(table='ex06_movies')
	return render(request, 'ex06/init.html', context={'msg': msg} )

def populate(request):
	result = []
	for d in data:
		msg = psy.insert_into_table(
                    epi_nb=d['epi_nb'],
                    title=d['title'],
                    director=d['director'],
                    producer=d['producer'],
                	rel_date=d['rel_date']
                )
		result.append(msg)
	return render(request, 'ex06/populate.html', context={'result': result} )


def display(request):
	records = psy.select_all_from_table(table='ex06_movies')
	col_names = list(map(lambda x: x[0].capitalize(), psy.get_column_names_from_table('ex06_movies')))
	col_names[0], col_names[1] = col_names[1], col_names[0]
	if type(records) == str:
		msg = records
		return render(request, 'ex06/display.html', context={'msg': msg} )

	return render(request, 'ex06/display.html', context={'records': records, 'col_names': col_names} )



def update(request):
	msg = ''
	if request.method == 'POST':
		form = forms.TitleDropDownForm(request.POST)
		if form.is_valid():
			# if error ?
			psy.update_movie(
				table='ex06_movies',
				title=form.cleaned_data['title'],
				val=form.cleaned_data['opening_crawl']
			)
		return redirect(request.META.get('HTTP_REFERER'))
	else:
		form = forms.TitleDropDownForm()

	if not form.reload():
		msg = "No data available."
	return render(request, 'ex06/update.html', context={'form' : form, 'msg' : msg})




