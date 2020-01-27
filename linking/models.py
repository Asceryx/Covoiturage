from django.db import models
from passengers.models import Passenger
from drivers.models import Driver, Path


class Proposal(models.Model):
	driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
	path = models.ForeignKey(Path, on_delete=models.CASCADE)

	def __str__(self):
		return "{} propose {}".format(self.driver,self.path)

	class Meta :	
		ordering =['driver']


class Candidate(models.Model):
	proposition = models.OneToOneField(Proposal, on_delete=models.CASCADE)
	passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
	validate = models.BooleanField()

	def __str__(self):
		return "{} for {} is validate({})".format(passenger,path, validate)

	class Meta :
		ordering = ['passenger']








