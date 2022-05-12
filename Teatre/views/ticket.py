from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Ticket, Client, MovieCinemaRoom
from django.http import HttpResponseRedirect
from django.urls import reverse
import random

@login_required
def ticket_select(request,**kwargs):
    if request.user.is_authenticated:
        datos = MovieCinemaRoom.objects.all()
        return render(request, 'Ticket/Select.html', {'datos':datos})
    else:
        return render(request,'Error/error_generico.html',{'error': {'title':'User not logged',
                                                                     'message': 'You need to log in to buy tickets'}})
@login_required
def ticket_buy(request,id_assignation):
    seats = list()
    client = Client.objects.get(user_id=request.user.id)
    movie_cinema_room = MovieCinemaRoom.objects.get(pk=id_assignation)
    room = movie_cinema_room.Room
    movie = movie_cinema_room.Movie
    cinema = movie_cinema_room.Cinema
    seats_busy = list()
    for tickets in Ticket.objects.all():
        if tickets.Room == room:
            for room_seat in tickets.Seats:
                seats_busy.append(room_seat)
    seat = random.randint(0, room.capacity)
    seats.append(seat)
    if request.method == 'POST':
        try:
            request.POST['save']
            for num_ticket in range(int(request.POST['num'])-1):
                seat = seat+1
                seats.append(seat)
            total = 8.5*len(seats)
            return render(request, 'Ticket/Buy.html',
                          {'movie_cinema_room': movie_cinema_room, 'seat': seats,'total':total,'number':len(seats)})

        except:
            for num_ticket in range(int(request.POST['buy'])-1):
                seat = seat+1
                seats.append(seat)
            total = 8.5 * len(seats)
            Ticket.objects.create(price=total,Movie=movie,Cinema=cinema,Room=room,date=movie_cinema_room.date_movie, Client=client,Seats=seats)
            tickets_obj = Ticket.objects.all()
            return HttpResponseRedirect(reverse('list_tickets'))
    else:
        total = 8.50 * len(seats)
        return render(request, 'Ticket/Buy.html', {'movie_cinema_room': movie_cinema_room, 'seat': seats,'total':total,'number':len(seats)})

@login_required
def ticket_list(request):
    tikets = Ticket.objects.filter(Client_id=request.user.id)
    return render(request,'Ticket/List.html',{'tickets':tikets})

@login_required
def ticket_detail(request,id_ticket):
    ticket = Ticket.objects.get(pk=id_ticket)
    return render(request,'Ticket/Detail.html',{'ticket':ticket})