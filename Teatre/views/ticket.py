from django.shortcuts import render
from Teatre.models import *


def ticket_list(request):
    tickets = Ticket.objects.all()
    json = {'tickets': tickets}
    return render(request, 'Ticket/List.html', json)
