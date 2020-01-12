from django.urls import path

from . import views

urlpatterns = [
    path('', views.driver, name='conducteur'),
    path('registration', views.registration, name='enregistrement')
]