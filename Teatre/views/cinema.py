from django.shortcuts import render
from Teatre.models import *

def CinemaDetail(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas': cinemas}
    return render(request, 'Cinema/Detail.html', json)

def CinemaList(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas': cinemas}
    return render(request, 'Cinema/List.html', json)
