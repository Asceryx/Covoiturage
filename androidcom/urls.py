from django.urls import path

from . import views

urlpatterns = [
    path('applogin/', views.auths, name='applogin'),
    path('appPath/passenger/', views.PassengerPath, name='appPathPassenger'),
    path('appPath/passenger/cancel/', views.CancelPath, name='appPathPassengerCancel'),
    path('appPath/passenger/search/', views.searchPath, name='appPathPassengerSearch'),
    path('appPath/driver/', views.DriverPath, name='appPathDriver'),
    path('appPath/driver/submit/', views.submitPath, name='appPathDriverSubmit'),
]