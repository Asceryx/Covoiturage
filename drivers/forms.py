from django import forms
from .models import Driver,Car,Location
from django.utils.timezone import now


class DriverRegistrationForm(forms.Form):
	email = forms.EmailField(label='Email', max_length=254)
	phone = forms.CharField(label='Numéro téléphone')
	vehicule = forms.CharField(label = 'Marque du véhicule', max_length=254)
	place_available = forms.IntegerField(label='Place disponible')
	

class DriverProposition(forms.Form):
	start = forms.ModelChoiceField(label='Départ', queryset=Location.objects.order_by("name").all())
	stop = forms.ModelChoiceField(label='Arrivée', queryset=Location.objects.order_by("name").all())
	datetime = forms.DateTimeField(label='Date', initial = now, input_formats=['%d/%m/%Y %H:%M'])
	passenger = forms.IntegerField(label = "Nombre de passager")
