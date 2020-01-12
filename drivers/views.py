from django.http import HttpResponse
from django.shortcuts import render
from .models import Driver,Car,Path
from linking.models import Proposal

from .forms import DriverForm

def driver(resquest):
	return HttpResponse("Main interface for driver")

def registration(request):
	if request.method == 'POST':
		form = DriverForm(request.POST)
		

		if form.is_valid():
			path = Path.objects.create(
				departure=form.cleaned_data['start'], 
				arrive= form.cleaned_data['stop'], 
				datedeparture = form.cleaned_data['datetime']
			)

			print(form.cleaned_data['datetime'])

			driver = Driver(
				user = request.user, 
				driver_path = path,
				email = form.cleaned_data['email'],
				phone = form.cleaned_data['phone']
			)
			driver.save()


			car  = Car.objects.create(
				vehicule = form.cleaned_data['car'], 
				place_available = form.cleaned_data['passenger'], 
				owner = driver
				)

			propose = Proposal.objects.create(
				driver= driver, 
				path = path
			)

			return HttpResponse('Job Done !!!')
	else:
		form = DriverForm()


	return render(request, 'drivers/registration.html', {'form': form})



