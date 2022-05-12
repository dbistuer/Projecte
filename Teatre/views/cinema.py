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
            return render(request, 'Cinema/new_room.html', {'success': False, 'cines': cines_list})
        Room.objects.create(capacity=capacity, number=number, Cinema_id=cine.id)
        return render(request, 'Cinema/new_room.html', {'success': True, 'cines': cines_list})
    else:
        return render(request, 'Cinema/new_room.html', {'success': '.', 'cines': cines_list})


def room_list(request, id_cinema):
    if request.method == 'GET':
        # Falta poner la pantalla de errores como dijo el profesor virgili para que no puedan mapear la bbdd (try, except)
        cine = Cinema.objects.get(id=id_cinema)
        rooms = Room.objects.filter(Cinema_id=cine.id)
        return render(request, 'Cinema/room_list.html', {'rooms': rooms, 'cinema': cine, 'cinema_id': id_cinema})


def modify_room(request,id_cinema ,id_room):
    if request.method == 'GET':

        rooms = Room.objects.filter(id=id_room,Cinema_id=id_cinema)

        # falta añadir el id del cineam para saber donde hago el return
        return render(request, 'Cinema/modify_room.html', {'rooms': rooms, 'cinema_id': id_cinema, 'room_id': id_room, 'room': rooms[0]})
    if request.method == 'POST':
        rooms = Room.objects.filter(id=id_room)
        room = Room.objects.get(id=id_room)
        if request.POST['Valor'] == 'modify':
            room.capacity = str(request.POST['capacity'])
            room.save()
            return render(request, 'Cinema/modify_room.html', {'rooms': rooms, 'cinema_id': id_cinema, 'room_id': id_room})
        if request.POST['Valor']== 'eliminar':
            room.delete()
            cine = Cinema.objects.get(id=id_cinema)
            rooms = Room.objects.filter(Cinema_id=cine.id)
            return render(request, 'Cinema/room_list.html', {'rooms': rooms, 'cinema': cine, 'cinema_id': id_cinema})
