
from django.db import models



# Create your models here.
"""
• name: unique, variable character chain, 64 byte maximum size, non null.
• climate: variable character chain.
• diameter: whole.
• orbital_period: whole.
• population: large whole.
• rotation_period: whole.
• surface_water: real.
• terrain: character chains.
• created a datetime type (date and time), that, when created, must automatically
set to the current date and time.
• updated a datetime type (date and time), that, when created, must automatically
set to the current date and time and automatically updates with each update.
This model also must redefine the __str__() method so that it returns the name
attribute.
"""

class Planets(models.Model):
	name = models.CharField(max_length=64, null=False, unique=True)
	climate = models.CharField(max_length=80, null=True)
	diameter = models.IntegerField(null=True)
	orbital_period = models.IntegerField(null=True)
	population = models.BigIntegerField(null=True)
	rotation_period = models.IntegerField(null=True)
	surface_water = models.FloatField(null=True)
	terrain = models.CharField(max_length=128, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class People(models.Model):
	name = models.CharField(max_length=64, null=False)
	birth_year = models.CharField(max_length=32, null=True)
	gender = models.CharField(max_length=32, null=True)
	eye_color = models.CharField(max_length=32, null=True)
	hair_color = models.CharField(max_length=32, null=True)
	height = models.IntegerField(null=True)
	mass = models.FloatField(null=True)
	homeworld = models.ForeignKey(to=Planets, on_delete=models.SET_NULL, null=True, db_column='homeworld') #to_field='name',
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name



"""
The second model you will create must be named People and contain the following
fields:
• name: character chain, 64 byte maximum size, non null.
• birth_year: character chain, 32 byte maximum size.
• gender: character chain, 32 byte maximum size.
• eye_color: character chain, 32 byte maximum size.
• hair_color: character chain, 32 byte maximum size.
• height: whole.
• mass: real.
• homeworld: character chain, 64 byte maximum size, foreign key referencing the
name column of this app’s Planets table.
• created a datetime type (date and time), that, when created, must automatically
set to the current date and time.
• updated a datetime type (date and time), that, when created, must automatically
set to the current date and time and automatically updates with each update.
This model also must redefine the __str__() method so that it returns the name
attribute.

"""
