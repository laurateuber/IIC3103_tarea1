from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola este es el index")
# Create your views here.
