from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate, login, logout

from django.core import serializers

from django.views import View



class DriverRequest(View)