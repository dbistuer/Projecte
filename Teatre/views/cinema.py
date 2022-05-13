from django.shortcuts import render, redirect
from Teatre.models import *

def Cinema_List(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas': cinemas, 'request': request}
    return render(request, 'Cinemas/List.html', json)

def Cinema_(request, **kwargs):
    id = int(kwargs.get('id'))
    cinema = Cinema.objects.get(id=id)
    json = {'cinema': cinema, 'request': request}
    if request.method == 'POST':
        type = kwargs.get('type')
    return render(request, 'Cinemas/cinema.html', json)


def New_Cinema(request):
    if not request.user.is_staff:
        return redirect('/Teatre/Cinemas/List')
    
    if request.method == 'POST':
        try:
            cinema = get_Cinema_from_attr(request)
        except Exception as e:
            return render(request, 'errorPage.html')
        cinema.save()
        return Cinema_List(request)
    return render(request, 'Cinemas/new_cinema.html')


def Cinema_Edit(request, id):    
    if not request.user.is_staff:
        return redirect('/Teatre/Cinemas/List')
    
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
    if request.user.is_staff:
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

@login_required
@user_passes_test(lambda user: user.is_staff)
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

@login_required
@user_passes_test(lambda user: user.is_staff)
def room_list(request, id_cinema):
    if request.method == 'GET':
        try:
            cine = Cinema.objects.get(id=id_cinema)
        except:
            return render(request, "error/error_generico.html", {'error': {
                'title': 'Esta pagina no existe',
                'message': 'O usted no tiene los permisos necesarios'
            }})
        rooms = Room.objects.filter(Cinema_id=cine.id)
        return render(request, 'Cinema/room_list.html', {'rooms': rooms, 'cinema': cine, 'cinema_id': id_cinema})

@login_required
@user_passes_test(lambda user: user.is_staff)
def modify_room(request,id_cinema ,id_room):
    if request.method == 'GET':
        try:
            rooms = Room.objects.filter(id=id_room,Cinema_id=id_cinema)
            return render(request, 'Cinema/modify_room.html', {'rooms': rooms, 'cinema_id': id_cinema, 'room_id': id_room, 'room': rooms[0]})
        except:
            return render(request, "error/error_generico.html", {'error': {
                'title': 'Esta pagina no existe',
                'message': 'O usted no tiene los permisos necesarios'
            }})
    if request.method == 'POST':
        rooms = Room.objects.filter(id=id_room)
        room = Room.objects.get(id=id_room)
        if request.POST['Valor'] == 'modify':
            room.capacity = str(request.POST['capacity'])
            room.save()
            return render(request, 'Cinema/modify_room.html', {'rooms': rooms, 'cinema_id': id_cinema, 'room_id': id_room,'room': rooms[0]})
        if request.POST['Valor']== 'eliminar':
            room.delete()
            cine = Cinema.objects.get(id=id_cinema)
            rooms = Room.objects.filter(Cinema_id=cine.id)
            return render(request, 'Cinema/room_list.html', {'rooms': rooms, 'cinema': cine, 'cinema_id': id_cinema})
