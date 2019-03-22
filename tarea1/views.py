from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse(requests.get('https://swapi.co/api/films').text)
# Create your views here.
