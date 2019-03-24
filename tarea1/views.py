from django.shortcuts import render
from django.http import HttpResponse
import requests
from tarea1.swapihelper import get_movies

def index(request):
    data = {'data': get_movies()}
    for movie in data['data']:
        movie['url_id'] = movie['url'].strip().split('/')[-1]
    return render(request, "index.html", data)
# Create your views here.

def movie(request, url_id):
    data = {'data': get_movie(url_id)}
