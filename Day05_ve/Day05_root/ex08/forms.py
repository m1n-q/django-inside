from django import forms
from django.forms import widgets
import psycopg2


class TitleDropDownForm(forms.Form):


	def get_title():
		try:
			conn = psycopg2.connect(database='djangotraining', user='djangouser', password='secret')
			try:
				cur = conn.cursor()
				cur.execute("""
					SELECT title FROM %s;
					""" % ('ex06_movies', )
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
	opening_crawl = forms.CharField(widget=forms.Textarea)

	def reload(self):
		titles = TitleDropDownForm.get_title()
		self.fields['title'] = forms.ChoiceField(choices=titles)
		if not titles:
			return 0
		return 1






