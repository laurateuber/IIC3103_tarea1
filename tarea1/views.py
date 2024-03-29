from django.shortcuts import render
from django.http import HttpResponse
import requests
from tarea1.swapihelper import get_movies, get_movie, get_character, get_planet, get_starship, get_search_results

def index(request):
    data = {'data': get_movies()}
    for movie in data['data']:
        movie['url_id'] = movie['url'].strip().split('/')[-2]
    return render(request, "index.html", data)

def movie(request, url_id):
    data = {'data': get_movie(url_id)}
    return render(request, "movie.html", data)

def people(request, url_id):
    data = {'data': get_character(url_id)}
    return render(request, "people.html", data)

def planet(request, url_id):
    data = {'data': get_planet(url_id)}
    return render(request, "planet.html", data)

def starship(request, url_id):
    data = {'data': get_starship(url_id)}
    return render(request, "starship.html", data)

def search(request):
    if 'q' in request.GET and request.GET["q"]!="":
        data = {'data': get_search_results(request.GET["q"])}
    else:
        data = {'data': {"message" : "You submitted an empty form. Please try again"}}
    return render(request, "search.html", data)
