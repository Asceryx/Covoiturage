from django import forms
from drivers.models import Location
	
from django.utils.timezone import now


class LinkingSearch(forms.Form):
	start = forms.ModelChoiceField(label='Départ', queryset=Location.objects.order_by("name").all())
	stop = forms.ModelChoiceField(label='Arrivée', queryset=Location.objects.order_by("name").all())
	datetime = forms.DateTimeField(label='Date', initial = now, input_formats=['%d/%m/%Y %H:%M'])