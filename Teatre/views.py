from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'cinemas/home.html')

def CinemaList(request):
    cinemas = Cinema.objects.all()
    for cinema in cinemas:
        cinema.room_set.all()
        for room in cinema.room_set:
            j=2
    rooms = Room.objects.all()
    for room in rooms:
        i = 0
    json = {'cinemas':cinemas}
    #TODO: GET ROMS
    return render(request, 'Cinema/List.html', json)

def MovieDetail(request):
    movies = Movie.objects.all()
    json = {'movies':movies}
    return render(request, 'Movie/Detail.html', json)

def MovieList(request):
    movies = Movie.objects.all()
    json = {'movies': movies}
    return render(request, 'Movie/List.html', json)

def ticket_list(request):
    #tickets = Ticket.objects.all()
    #json = {'tickets', tickets}
    return render(request, 'Ticket/ticketList.html')

def SignIn(request):
    if request.method == 'POST':
        return render(request, 'registration/login.html',{'client':CreateClient(request)})
    else:
        return render(request, 'registration/SignIn.html')

def GetElementFromRequest(request,name):
    return request.POST[name]

def CreateClient(request):
    name = GetElementFromRequest(request, 'name')
    adress = GetElementFromRequest(request, 'adress')
    telephone = GetElementFromRequest(request, 'telephone')
    cardNumber = GetElementFromRequest(request, 'cardNumber')
    email = GetElementFromRequest(request, 'email')
    DNI = GetElementFromRequest(request, 'DNI')
    alias = GetElementFromRequest(request, 'alias')
    password = GetElementFromRequest(request, 'password')
    return Client.objects.create(name=name,adress=adress,telephone=telephone,
                                 cardNumber=cardNumber,email=email,DNI=DNI,
                                 alias=alias,password=password,user=CreateBaseUser(alias,email,password))

def CreateBaseUser(alias,email,password):
    return User.objects.create_user(alias,email,password)