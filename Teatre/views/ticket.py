from django.shortcuts import render
from ..models import Ticket, Client, MovieCinemaRoom
from django.http import HttpResponseRedirect
from django.urls import reverse
import random


def ticket_select(request,**kwargs):
    if request.user.is_authenticated:
        datos = MovieCinemaRoom.objects.all()
        return render(request, 'Ticket/Select.html', {'datos':datos})
    else:
        return render(request,'Error/error_generico.html',{'error': {'title':'User not logged',
                                                                     'message': 'You need to log in to buy tickets'}})

def ticket_buy(request,id_assignation):
    client = Client.objects.get(user_id=request.user.id)
    movie_cinema_room = MovieCinemaRoom.objects.get(pk=id_assignation)
    room = movie_cinema_room.Room
    movie = movie_cinema_room.Movie
    cinema = movie_cinema_room.Cinema
    seats_busy = list()
    for tickets in Ticket.objects.all():
        if tickets.Room == room:
            seats_busy.append(tickets.Seat)
    seat = random.randint(0, room.capacity)
    if request.method == 'POST':
        Ticket.objects.create(date=movie_cinema_room.date_movie, Seat=seat, Client=client, Movie=movie,Cinema=cinema,Room=room )
        tickets_obj = Ticket.objects.all()
        return HttpResponseRedirect(reverse('list_tickets'))
    else:
        return render(request, 'Ticket/Buy.html', {'movie_cinema_room': movie_cinema_room, 'seat': seat})


def ticket_list(request):
    tikets = Ticket.objects.filter(Client_id=request.user.id)
    return render(request,'Ticket/List.html',{'tickets':tikets})
