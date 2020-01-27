from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Driver,Car,Path
from linking.models import Proposal

from .forms import DriverProposition,DriverRegistrationForm
from django.contrib.auth.decorators import login_required,permission_required


@login_required()
def profil(request):
	profil = Driver.objects.filter(user = request.user)
	if profil.exists():
		return HttpResponse("Main interface for <strong>existing</strong> driver")
	else:
		if request.method == 'POST':
			form = DriverRegistrationForm(request.POST)
		
			if form.is_valid():
				driver = Driver.objects.create(
					user = request.user, 
					email = form.cleaned_data['email'],
					phone = form.cleaned_data['phone']
				)

				car  = Car.objects.create(
					vehicule = form.cleaned_data['vehicule'], 
					place_available = form.cleaned_data['place_available'], 
					owner = driver
				)

				return redirect('profil')
		else:
			form = DriverRegistrationForm()

		return HttpResponse("Main interface for <strong>registration</strong> driver")
		#return render(request, 'drivers/registration.html', {'form': form})

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

	#
	


@login_required()
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



