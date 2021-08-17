from django import forms

class MessageForm(forms.Form):
	message = forms.CharField(max_length=5, label='Message')

class NameForm2(forms.Form):
	your_name = forms.CharField(max_length=5, label='TEST')


	'''

	<label for="your_name">YOUR NAME: </label>
	<input id="your_name" type="text" name="your_name" maxlength="100" required>

	* Note that it does not include the <form> tags, or a submit button. We’ll have to provide those ourselves in the template.

	Form data sent back to a Django website is processed by a view,
	generally the same view which published the form. This allows us to reuse some of the same logic.

	'''
