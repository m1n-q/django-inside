from django.shortcuts import render

# Create your views here.
def mainpage(request):

	# ver. shade
	# return render(request, 'ex03/mainpage.html', context={'range' : range(50, -1, -1), 'cell': 5.1})

	# ver. alpha
	return render(request, 'ex03/mainpage.html', context={'range' : range(100, 0, -2), 'cell': 5.1})
