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
