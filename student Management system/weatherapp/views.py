from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

import requests
import datetime


def index(request):
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=23eb060477212233b60ed3b3147f9a18'
    return render(request, 'weatherapp/index.html')