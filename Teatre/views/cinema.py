from django.shortcuts import render, redirect
from Teatre.models import *

def Cinema_List(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas': cinemas, 'request': request}
    return render(request, 'Cinemas/List.html', json)

def Cinema_(request, **kwargs):
    id = int(kwargs.get('id'))
    cinema = Cinema.objects.get(id=id)
    json = {'cinema': cinema}
    if request.method == 'POST':
        type = kwargs.get('type')
    return render(request, 'Cinemas/cinema.html', json)


def New_Cinema(request):
    if request.method == 'POST':
        try:
            cinema = get_Cinema_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        cinema.save()
        return Cinema_List(request)
    return render(request, 'Cinemas/new_cinema.html')


def Cinema_Edit(request, id):
    cinema = 0
    try:
        cinema = Cinema.objects.get(pk=id)
    except Exception as e:
        return render(request, 'errorPage.html')
    if request.method == 'POST':
        try:
            cinema_edit = get_Cinema_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        Cinema.objects.filter(id__exact=id).update(name=request.POST.get('name', False))
        Cinema.objects.filter(id__exact=id).update(adress=request.POST.get('adress', False))
        Cinema.objects.filter(id__exact=id).update(description=request.POST.get('description', False))
        return redirect('/Teatre/Cinemas/List')
    json = {'cinema': cinema}
    return render(request, 'Cinemas/new_cinema.html', json)
    
def Cinema_Delete(request, id):
    cinema = 0
    try:
        cinema = Cinema.objects.get(pk=id)
    except Exception as e:
        return render(request, 'errorPage.html')
        Cinema.objects.update(cinema_edit)
        cinema = cinema_edit
    cinema.delete()
    return redirect('/Teatre/Cinemas/List')


def get_Cinema_from_attr(request):
    try:
        name = request.POST['name']
        adress = request.POST['adress']
        description = request.POST['description']
    except Exception as e:
        return e
    return Cinema(name=name, adress=adress, description=description)
