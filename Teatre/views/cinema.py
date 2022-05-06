from django.shortcuts import render
from Teatre.models import *


def CinemaList(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas': cinemas}
    return render(request, 'Cinema/List.html', json)
