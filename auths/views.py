from django.shortcuts import render, redirect
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.http import JsonResponse



def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:  
                login(request, user)
                return redirect(reverse('home'))
            else: 
                error = True

    else:
        form = ConnexionForm()

    return render(request, 'auths/authentification.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))




