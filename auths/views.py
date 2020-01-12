from django.shortcuts import render, redirect
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def connexion(request):
    error = False
    redirect_to = request.REQUEST.get('next', '')
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:  
                login(request, user)
            else: 
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'auths/authentification.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


