from django.shortcuts import render
from .models import Proposal

from django.utils import timezone

# Create your views here.

def proposal_listing(request):
	propositions = Proposal.objects.filter(path__datedeparture__gte=timezone.now())
	print(propositions)

	return render(request, 'linking/proposition.html', {'propositions': propositions})