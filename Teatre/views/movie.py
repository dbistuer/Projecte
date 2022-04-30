from django.shortcuts import render
from Teatre.models import *
from Projecte.settings.base import MEDIA_ROOT
#TODO: DELETE UPPER LINE

def MovieDetail(request):
    movies = Movie.objects.all()
    json = {'movies': movies}
    return render(request, 'Movie/Detail.html', json)


def MovieList(request):
    movies = Movie.objects.all()
    json = {'movies': movies,'MEDIA_ROOT':MEDIA_ROOT}
    return render(request, 'Movie/List.html', json)

def Movie_(request,**kwargs):
    id = int(kwargs.get('id'))
    movie = Movie.objects.get(id=id)
    json = {'movie': movie}
    if request.method == 'POST':
        type = kwargs.get('type')
    return render(request,'Movie/movie.html',json)
