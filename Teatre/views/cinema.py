from django.shortcuts import render
from Teatre.models import *

def Cinema_List(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas': cinemas}
    return render(request, 'Cinema/List.html', json)

def Cinema_(request, **kwargs):
    id = int(kwargs.get('id'))
    cinema = Cinema.objects.get(id=id)
    json = {'cinema': cinema}
    if request.method == 'POST':
        type = kwargs.get('type')
    return render(request, 'Cinema/cinema.html', json)


def New_Cinema(request):
    if request.method == 'POST':
        try:
            cinema = get_Cinema_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        cinema.save()
        return Cinema_List(request)
    return render(request, 'Movie/new_cinema.html', {'api_url': API_MOVIEDB_URL, 'api_key': API_MOVIEDB_KEY, })
    #TODO adaptar aixo


def Cinema_Edit(request, id):
    cinema = 0
    try:
        cinema = cinema.objects.get(pk=id)
    except Exception as e:
        return render(request, 'errorPage.html')
    if request.method == 'POST':
        try:
            cinema_edit = get_Cinema_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        Cinema.objects.update(cinema_edit)
        cinema = cinema_edit
    return render(request, 'Cinema/new_cinema.html',
                  {'api_url': API_MOVIEDB_URL, 'api_key': API_MOVIEDB_KEY, 'movie': movie})


def get_Cinema_from_attr(request):
    try:
        name = request.POST['name']
        address = request.POST['address']
        description = request.POST['description']
    except Exception as e:
        return e
    return Movie(name=name, address=address, description=description)
