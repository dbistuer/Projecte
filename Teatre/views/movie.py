from django.shortcuts import render
from Teatre.models import *
from Projecte.settings.base import MEDIA_ROOT, API_MOVIEDB_KEY, API_MOVIEDB_URL
# TODO: DELETE UPPER LINE

def MovieDetail(request):
    movies = Movie.objects.all()
    json = {'movies': movies}
    return render(request, 'Movie/Detail.html', json)


def Movie_List(request):
    movies = Movie.objects.all()
    json = {'movies': movies, 'MEDIA_ROOT': MEDIA_ROOT}
    return render(request, 'Movie/List.html', json)


def Movie_(request, **kwargs):
    id = int(kwargs.get('id'))
    movie = Movie.objects.get(id=id)
    json = {'movie': movie}
    if request.method == 'POST':
        type = kwargs.get('type')
    return render(request, 'Movie/movie.html', json)


def New_Movie(request):
    if request.method == 'POST':
        try:
            movie = get_Movie_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        movie.save()
        return Movie_List(request)
    return render(request, 'Movie/new_movie.html', {'api_url': API_MOVIEDB_URL, 'api_key': API_MOVIEDB_KEY, })


def Movie_Edit(request, id):
    movie = 0
    try:
        movie = Movie.objects.get(pk=id)
    except Exception as e:
        return render(request, 'errorPage.html')
    if request.method == 'POST':
        try:
            movie_edit = get_Movie_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        Movie.objects.update(movie_edit)
        movie = movie_edit
    return render(request, 'Movie/new_movie.html',
                  {'api_url': API_MOVIEDB_URL, 'api_key': API_MOVIEDB_KEY, 'movie': movie})


def get_Movie_from_attr(request):
    try:
        name = request.POST['name']
        gender = request.POST['gender']
        classification = request.POST['classification']
        duration = int(request.POST['duration'])
        synopsis = request.POST['synopsis']
        image = request.POST['image']
    except Exception as e:
        return e
    return Movie(name=name, gender=gender, classification=classification, duration=duration, image=image,
                 synopsis=synopsis)
