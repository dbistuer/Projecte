
from django.shortcuts import render
from Teatre.models import *


def home(request):
    tickets = Ticket.objects.all()
    json = {'tickets': tickets}
    return render(request, 'home.html', json)
