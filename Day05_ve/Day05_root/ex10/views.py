from django.shortcuts import redirect, render
from .forms import SearchingForm
from . import models

# Create your views here.
def ex10(request):

	form = SearchingForm(request.GET)
	if form.is_valid():
		if form.cleaned_data['rel_date_min'] > form.cleaned_data['rel_date_max']:
			return redirect('ex10:display')
		res = []
		movies = models.Movies.objects.filter(
									# characters__gender__exact=form.cleaned_data['gender'],
									# characters__homeworld__diameter__gt=form.cleaned_data['diameter'],
									release_date__gt=form.cleaned_data['rel_date_min'],
									release_date__lt=form.cleaned_data['rel_date_max'],
								).all()
		for movie in movies:
			characters = movie.characters.filter(
							gender__exact=form.cleaned_data['gender'],
							homeworld__diameter__gt=form.cleaned_data['diameter']
						)
			for character in characters:
				res.append([
					movie.title,
					character.name,
					character.gender,
					character.homeworld.name,
					character.homeworld.diameter
				])

		return render(request, 'ex10/ex10.html', context={'form':form, 'res':res})

	else:
		print('not valid')


	return render(request, 'ex10/ex10.html', context={'form':form})
