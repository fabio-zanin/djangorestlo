from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def sobre(requeste):
    return HttpResponse('Sobre')


def contato(request):
    return HttpResponse('Contato')
