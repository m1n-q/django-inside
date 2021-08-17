from django.shortcuts import redirect, render
from . import psy, forms
from datetime import date


def init(request):
	msg = []
	msg.append(psy.create_planets_table(table='ex08_planets'))
	msg.append(psy.create_people_table(table='ex08_people'))
	return render(request, 'ex08/init.html', context={'msg': msg} )

def populate(request):
	result = psy.file_to_table()
	return render(request, 'ex08/populate.html', context={'result': result} )


def display(request):
	joined = list(map(lambda x: x[0].split('"')[1:-1] ,psy.join_table()))
	joined = list(map(lambda x: list(map(lambda y: y.strip(',') ,x)) , joined))
	print(joined)


	# pl_err = False
	# pl_records = psy.select_all_from_table(table='ex08_planets')
	# pl_col_names = list(map(lambda x: x[0].capitalize(), psy.get_column_names_from_table('ex08_planets')))



	# pp_err = False
	# pp_records = psy.select_all_from_table(table='ex08_people')
	# pp_col_names = list(map(lambda x: x[0].capitalize(), psy.get_column_names_from_table('ex08_people')))


	# if type(pl_records) == str:
	# 	pl_err = True
	# if type(pp_records) == str:
	# 	pp_err = True
	return render(request, 'ex08/display.html',
				context={
					# 'pl_records': pl_records,
					# 'pp_records': pp_records,
	 				# 'pl_col_names': pl_col_names,
	 				# 'pp_col_names': pp_col_names,
					# 'pl_err': pl_err,
					# 'pp_err': pp_err,
					'joined': joined,
				}
		)
