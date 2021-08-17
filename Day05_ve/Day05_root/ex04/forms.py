from django import forms
from django.forms.fields import ChoiceField
import psycopg2


class TitleDropDownForm(forms.Form):
	# <option>
	CHOICES = [
		# val , text
		('The Phantom Menace', 'The Phantom Menace'),
		('Attack of the Clones', 'Attack of the Clones'),
		('Revenge of the Sith', 'Revenge of the Sith'),
		('A New Hope', 'A New Hope'),
		('The Empire Strikes Back', 'The Empire Strikes Back'),
		('Return of the Jedi', 'Return of the Jedi'),
		('The Force Awakens', 'The Force Awakens'),
	]


	def get_title():
		try:
			conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
			try:
				cur = conn.cursor()
				cur.execute("""
					SELECT title FROM %s;
					""" % ('ex04_movies', )
				)
				res = cur.fetchall()
			except Exception as e:
				return []
			else:
				conn.commit()
				conn.close()
				cur.close()
				ret = []
				for tup in res:
					ret.append((tup[0], tup[0]))
				return ret

		except Exception as e:
			return []

	title = forms.ChoiceField(choices=get_title())

	def reload(self):
		# name = <select>
		# TitleDropDownForm.title = forms.ChoiceField(label='Select', choices=TitleDropDownForm.get_title())

		titles = TitleDropDownForm.get_title()
		self.fields['title'] = forms.ChoiceField(choices=titles)
		if not titles:
			return 0
		return 1






