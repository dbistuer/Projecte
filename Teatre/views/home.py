from django.shortcuts import render
from Teatre.models import *


def home(request):
    movie = Movie.objects.get(name='Hola')
    return render(request, 'home.html', {'movie': movie})
