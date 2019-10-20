from django.shortcuts import render
from django.http import HttpResponse



def hola(request, nombre):
    return HttpResponse("Hola, " + nombre )
