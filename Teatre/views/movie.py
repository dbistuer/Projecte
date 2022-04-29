from django.shortcuts import render
from Teatre.models import *

def MovieDetail(request):
    movies = Movie.objects.all()
    json = {'movies':movies}
    return render(request, 'Movie/Detail.html', json)

def MovieList(request):
    movies = Movie.objects.all()
    json = {'movies': movies}
    return render(request, 'Movie/List.html', json)