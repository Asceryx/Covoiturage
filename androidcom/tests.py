from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


class ClientAuthsTest(TestCase):
	def setUp(self):
		User.objects.get_or_create('John', 'John.Doe@mail.com', 'JDsecret')

	def test_client_can_be_authenticate(self):
		response = self.client.get('/applogin/?id=John&password=JDsecret')
		self.assertTrue(response.json()['result'] and User.is_authenticated())



class ClientDriverTestProposition(TestCase):

	def setUp(self):
		self.client.force_login('John')

	def test_driver_made_proposition(self):
		response = self.client.get('appPath/driver/submit/?id=John&depart=Marie%20Curie&arrive=Rabelais&heure=2019-11-22%2017:52&prix=40&places=4')
		self.assertTrue(response.json()['result'])
		self.assertEqual(Path.objects.count(), 1)
		self.assertEqual(Proposal.objects.count(), 1)

	def test_driver_show_proposition(self):
		None

