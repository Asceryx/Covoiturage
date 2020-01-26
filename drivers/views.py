from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Driver,Car,Path
from linking.models import Proposal

from .forms import DriverProposition

def registration(request):
	"""
	driver = Driver(
		user = request.user, 
		driver_path = path,
		email = form.cleaned_data['email'],
		phone = form.cleaned_data['phone']
	)


	car  = Car.objects.create(
		vehicule = form.cleaned_data['car'], 
		place_available = form.cleaned_data['passenger'], 
		owner = driver
	)

	driver.save()
"""
	return HttpResponse("Main interface for driver")

def profil(request):
	None

def submit(request):
	if request.method == 'POST':
		form = DriverProposition(request.POST)
		
		if form.is_valid():
			path = Path.objects.create(
				departure=form.cleaned_data['start'], 
				arrive= form.cleaned_data['stop'], 
				datedeparture = form.cleaned_data['datetime']
			)

			driver = Driver.objects.get(user= request.user)

			propose = Proposal.objects.create(
				driver= driver, 
				path = path
			)

			return redirect('home')
	else:
		form = DriverProposition()


	return render(request, 'drivers/registration.html', {'form': form})



