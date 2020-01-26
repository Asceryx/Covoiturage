from django.urls import path

from . import views

urlpatterns = [
    path('', views.registration, name='conducteur'),
    path('soumettre', views.submit, name='submit')
]