from django.shortcuts import render, redirect
from django.contrib import messages
import requests

# Create your views here.

def index(request):
    data = True
    result = None
    countries = None;
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            countries = json['Countries']

            data = False
        except:
            data = True
    return render(request, 'index.html', {'countries' : countries})