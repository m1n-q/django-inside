from django.shortcuts import render
from .forms import MessageForm
from django.http import HttpResponseRedirect
from django.utils import timezone
import logging

'''
	Form data sent back to a Django website is processed by a view,
	generally the same view which published the form. This allows us to reuse some of the same logic.
	To handle the form we need to instantiate it in the view for the URL where we want it to be published:
'''

logger = logging.getLogger(__name__)

def	load_history():
	f = open('ex02/logs', 'r')
	history = f.readlines()
	f.close()
	return history


def mainpage(request):

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = MessageForm(request.POST, label_suffix="")
		if form.is_valid():
			logger.debug(msg=form.cleaned_data['message'])
			# return HttpResponseRedirect('/ex02/')

	else:	# if 'GET' or other methods, we'll create blank form
		# form = NameForm2()
		form = MessageForm(label_suffix="")
	history = load_history()

	#return render(request, 'ex02/mainpage.html', {'form' : form, 'what_is_context':'나는민규에욤'})
	return render(request, 'ex02/mainpage.html', {'form' : form, 'history' : history })



'''
	If we arrive at this view with a GET request, it will create an empty form instance and place it in the template context to be rendered.
	This is what we can expect to happen the first time we visit the URL.

	If the form is submitted using a POST request, the view will once again create a form instance and populate it with data from the request:
	form = NameForm(request.POST)

	This is called “binding data to the form” (it is now a bound form).


	We call the form’s is_valid() method;
	if it’s not True, we go back to the template with the form.
	This time the form is no longer empty (unbound)
	so the HTML form will be populated with the data previously submitted, where it can be edited and corrected as required.

	If is_valid() is True, we’ll now be able to find all the validated form data in its cleaned_data attribute.
	We can use this data to update the database or do other processing before sending an HTTP redirect to the browser telling it where to go next.
'''
