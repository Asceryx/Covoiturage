from django.urls import path

from . import views

urlpatterns = [
    path('', views.proposal_listing, name='proposition'),
    path('rechercher', views.research, name='search')
]