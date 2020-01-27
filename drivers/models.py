from django.db import models
from django.contrib.auth.models import User
from passengers.models import Passenger



class Location(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return "{}".format(self.name)

class Path(models.Model):
	departure = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='requests_depart')
	arrive =  models.ForeignKey(Location, on_delete=models.CASCADE, related_name='requests_arrive')
	datedeparture = models.DateTimeField()

	def __str__(self):
		return "{} -> {}".format(self.departure,self.arrive)

	def CheckDate(self):
		"Return boolean if entry's date and hour is good"
		import datetime
		return self.datedeparture < datetime.now()



class Driver(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)


	def __str__(self):
		return "{}".format(self.user)

	class Meta :	
		ordering =['user']
		permissions = [
		('can_propose_path', 'Driver can propose a path'),
		('can_see_candidate', 'Driver can see candidate for a path'),
		('can_validate_candidate', 'Driver can validate candidate for a path')
		]


class Car(models.Model):
	vehicule = models.CharField(max_length=200)
	place_available = models.IntegerField(default=0)
	owner = models.OneToOneField(Driver, on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.vehicule)