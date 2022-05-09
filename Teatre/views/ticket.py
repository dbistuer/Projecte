from django.shortcuts import render
from ..models import Ticket, Client, Movie
import random


def ticket_buy(request,**kwargs):
    if request.method == 'POST':
        for compras in kwargs['num']:
            client = Client.objects.filter(user_id=request.user.id)
            #sala = agafar relacio movie_cinema_room
            #film = agafar relacio movie_cinema_room
            #cinema = agafar relacio movie_cinema_room
            seats_busy = list()
            for tickets in Ticket.objects.all():
                if tickets.Room == sala:
                    seats_busy.append(tickets.Seat)
            seat = random.randint(0,sala.capacity)
            return render(request, '')
    else:
        movies = Movie.objects.all()
        return render(request,'Ticket/Buy.html',{'movies':movies})

def ticket_list(request):
    tikets = Ticket.objects.all()
    return render(request,'Ticket/List.html')
