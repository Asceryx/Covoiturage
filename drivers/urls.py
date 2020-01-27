from django.urls import path

from . import views

urlpatterns = [
    path('', views.profil, name='conducteur'),
    path('soumettre', views.submit, name='submit')
]