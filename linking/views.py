from .models import Proposal
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from drivers.models import Path
from datetime import timedelta
from .forms import LinkingSearch

from django.contrib.auth.decorators import login_required

@login_required()
def proposal_listing(request):
	propositions = Proposal.objects.filter(path__datedeparture__gte=timezone.now())
	return render(request, 'linking/proposition.html', {'propositions': propositions})

@login_required()
def research(request):
	if request.method == 'POST':
		form = LinkingSearch(request.POST)
		
		if form.is_valid():
			time = form.cleaned_data['datetime']
			propositions = Proposal.objects.filter(
				path__departure = form.cleaned_data['start'],
				path__arrive = form.cleaned_data['stop'],
				path__datedeparture__gte = time - timedelta(hours=3), 
				path__datedeparture__lte = time + timedelta(hours=3)
				)
			propositions.filter(path__datedeparture__gte=timezone.now())
			return render(request, 'linking/proposition.html', {'propositions': propositions})
	else:
		form = LinkingSearch()

	return render(request, 'linking/search.html', {'form': form})




