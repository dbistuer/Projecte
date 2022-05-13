from django.shortcuts import render
from Teatre.models import *
from Projecte.settings.base import MEDIA_ROOT, API_MOVIEDB_KEY, API_MOVIEDB_URL
from django.contrib.auth.decorators import login_required, permission_required
# TODO: DELETE UPPER LINE

def MovieDetail(request):
    movies = Movie.objects.all()
    json = {'movies': movies}
    return render(request, 'Movie/Detail.html', json)


def Movie_List(request):
    movies = Movie.objects.all()
    json = {'movies': movies, 'MEDIA_ROOT': MEDIA_ROOT}
    return render(request, 'Movie/List.html', json)


def Detail_Movie(request, **kwargs):
    id = int(kwargs.get('id'))
    movie = Movie.objects.get(id=id)
    json = {'movie': movie}
    if request.method == 'POST':
        type = kwargs.get('type')
    return render(request, 'Movie/movie.html', json)


@login_required
def New_Movie(request):
    if user.is_active:
        return render(request, 'errorPage.html')
    json = {'api_url': API_MOVIEDB_URL, 'api_key': API_MOVIEDB_KEY, }
    if request.method == 'POST':
        try:
            movie = get_Movie_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        movie.save()
        json['mssg'] = 'Your movie has been added succesfuly.'
    return render(request, 'Movie/new_movie.html', json)

@login_required
def Movie_Edit(request, id):
    if user.is_active:
        return render(request, 'errorPage.html')
    movie = 0
    json = {'api_url': API_MOVIEDB_URL, 'api_key': API_MOVIEDB_KEY, 'movie': movie}
    try:
        movie = Movie.objects.get(pk=id)
        json['movie'] = movie
    except Exception as e:
        return render(request, 'errorPage.html')
    if request.method == 'POST':
        try:
            movie_edit = get_Movie_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        json['movie'] = update_movie_by_another(movie,movie_edit)
        json['mssg'] = 'Your changes have been saved succesfuly.'
    return render(request, 'Movie/new_movie.html',json)

@login_required
def Movie_Delete(request,id):
    if user.is_active:
        return render(request, 'errorPage.html')
    movie = Movie.objects.get(pk=id)
    if movie:
        movie.delete()
        return Movie_List(request)
    else:
        return render(request, 'errorPage.html')


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

def update_movie_by_another(to,from_):
    if from_.name != to.name and from_.name != '':
        to.name = from_.name
    if from_.gender != to.gender and from_.gender != '':
        to.gender = from_.gender
    if from_.duration != to.duration and from_.duration != 0:
        to.duration = from_.duration
    if from_.synopsis != to.synopsis and from_.synopsis != '':
        to.name = from_.synopsis
    if from_.classification != to.classification and from_.classification != '':
        to.classification = from_.classification
    if from_.image != to.image and from_.image != '':
        to.image = from_.image
    to.save()
    return to

