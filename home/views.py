from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='home')
def accueil(request):
	return render(request, 'home/accueil.html')