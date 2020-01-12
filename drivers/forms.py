from django import forms
from .models import Driver,Car,Location
from django.utils.timezone import now


class DriverForm(forms.Form):
	email = forms.EmailField(label='Email', max_length=254)
	phone = forms.CharField(label='Numéro téléphone')
	start = forms.ModelChoiceField(label='Départ', queryset=Location.objects.order_by("name").all())
	stop = forms.ModelChoiceField(label='Arrivée', queryset=Location.objects.order_by("name").all())
	datetime = forms.DateTimeField(label='Date', initial = now)
	car = forms.CharField(label = 'Véhicule')
	passenger = forms.IntegerField(label = "Nombre de passager")