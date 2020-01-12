from django.db import models
from django.contrib.auth.models import User


class Passenger(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)


	def __str__(self):
		return "{}".format(self.user)
