from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from datetime import time
import json
from drivers.models import Location, Path


class ClientAuthsTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user('John', 'John.Doe@mail.com', 'JDsecret')

	def test_client_can_be_authenticate(self):
		response = self.client.get('/applogin/?id=John&password=JDsecret')
		self.assertTrue(response.json()['result'] and self.user.is_authenticated())



class ClientDriverTestProposition(TestCase):
	def setUp(self):
		user = User.objects.create_user('John', 'John.Doe@mail.com', 'JDsecret')
		self.client.force_login(user)
		depart = Location.objects.create(name='Marie Curie')
		arrive = Location.objects.create(name='Rabelais')
		Path.objects.create(departure=depart, arrive = arrive, datedeparture=time())
		Driver.objects.create(user=user)

	def test_driver_made_proposition(self):
		response = self.client.get('appPath/driver/submit/?id=John&depart=Marie%20Curie&arrive=Rabelais&heure=2019-11-22%2017:52&prix=40&places=4')
		self.assertTrue(response.json()['result'])
		self.assertEqual(Path.objects.count(), 1)
		self.assertEqual(Proposal.objects.count(), 1)

