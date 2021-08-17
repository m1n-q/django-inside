from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import fields
from . import models


# Form.is_valid()
#	┗━━━ Form.clean()
#	  ┗━━━ Form.clean_<fieldname>() on each fields
#		┗━━━ Field.clean() -> { cleaned_data }
#		  ├─ to_python() on field
#		  ├─ validate() on field
# 	  	  └─ run_validator() on field

class SignUpForm(forms.Form):
	# class Meta:
	# 	model = User
	# 	fields = ['username', 'password']

	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)
	verif_password = forms.CharField(required=True, widget=forms.PasswordInput)


	def clean(self):
		cleaned = super().clean()
		username = cleaned['username']
		pw1 = cleaned['password']
		pw2 = cleaned['verif_password']


		if models.User.objects.filter(username__exact=username):
			self.add_error('username', "Username already exists :(")
		if pw1 != pw2:
			self.add_error('verif_password', "Check Password :(")
			# raise ValidationError("ERROR !!!!!")

			# forms.Form :
			# 이 단계의 오류를 보고하는 두 가지 방법이 있습니다.
			# 아마도 가장 일반적인 방법은 양식 상단에 오류를 표시하는 것입니다.
			# 이러한 오류를 생성하려면 ValidationError에서 발생시킬 수 있습니다	(non field eror)
			#
			#  Note that add_error() automatically removes the field from cleaned_data.

			# ModelForm
			# class ArticleForm(ModelForm):
			# class Meta:
			#     error_messages = {
			#         NON_FIELD_ERRORS: {
			#             'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			#         }
			#     }

		# return cleaned


class SignInForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)

	def clean(self):
		cleaned = super().clean()
		user = authenticate(username=cleaned['username'], password=cleaned['password'])
		if not user:
			raise ValidationError('Invalid Login')


class TipForm(forms.ModelForm):
	class Meta:
		model = models.Tip
		# fields = '__all__'
		fields = [
			'content',
		]
		# labels = {
		# 	'content': ,
		# }

	def __init__(self, *args, **kargs):
		super(TipForm, self).__init__(*args, **kargs)
		self.fields['content'].widget.attrs['placeholder'] = '내용을 입력하세요...'
