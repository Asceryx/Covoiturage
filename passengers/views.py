from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


@login_required()
def passenger(request):
	return HttpResponse("Main interface for passenger")
