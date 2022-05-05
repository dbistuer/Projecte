from django.shortcuts import render
from Teatre.models import *


def CinemaList(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas': cinemas}
    return render(request, 'Cinema/List.html', json)


def Create_sala(request):
    cines_list = list()
    for cin in Cinema.objects.all():
        cines_list.append(cin)

    if request.method == 'POST':
        capacity = request.POST['capacity']
        number = request.POST['number']
        if str.isdigit(request.POST['cinema']):
            cine = Cinema.objects.get(pk=request.POST['cinema'])

        else:
            return render(request, 'Cinema/new_room.html',{'success': False, 'cines' : cines_list})
        Room.objects.create(capacity=capacity,number=number,Cinema_id=cine.id)
        return render(request, 'Cinema/new_room.html',{'success': True, 'cines': cines_list})
    else:
        return render(request, 'Cinema/new_room.html',{'success': '.', 'cines': cines_list})


def room_list(request, id_cinema):
    if request.method == 'GET':
        cine = Cinema.objects.get(id=id_cinema )
        rooms = Room.objects.filter(Cinema_id=cine.id)
        return render(request,'Cinema/room_list.html',{'rooms': rooms, 'cinema' : cine})

