from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'cinemas/home.html')

def CinemaList(request):
    cinemas = Cinema.objects.all()
    rooms = Room.objects.all()
    json = {'cinemas':cinemas,
            'rooms':rooms}
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
    return render(request, 'Ticket/List.html')

def SignIn(request):
    if request.method == 'POST':
        return render(request, 'registration/login.html',{'client':CRUDClient(request,Method.INSERT)})
    else:
        return render(request, 'registration/SignIn.html')

def UserEdit(request,id):
    if request.method == 'GET':
        return render(request, 'User/Edit.html',{'client':Client.objects.get(id=id),'user':User.objects.get(id=id)})
    elif request.method == 'POST':
        CRUDClient(request,Method.UPDATE)

def GetElementFromRequest(request,name):
    return request.POST[name]

def CRUDClient(request,Method):
    name = GetElementFromRequest(request, 'name')
    adress = GetElementFromRequest(request, 'adress')
    telephone = GetElementFromRequest(request, 'telephone')
    cardNumber = GetElementFromRequest(request, 'cardNumber')
    email = GetElementFromRequest(request, 'email')
    DNI = GetElementFromRequest(request, 'DNI')
    alias = GetElementFromRequest(request, 'alias')
    password = GetElementFromRequest(request, 'password')
    if Method == Method.INSERT:
        return Client.objects.create(name=name,adress=adress,telephone=telephone,
                                 cardNumber=cardNumber,DNI=DNI,
                                 alias=alias,password=password,user=CRUDBaseUser(alias,email,password,Method))
    elif Method == Method.UPDATE:
        client = Client.objects.get(id=GetElementFromRequest(request,'id'))
        return client.update(name=name,adress=adress,telephone=telephone,
                                 cardNumber=cardNumber,DNI=DNI,alias=alias,password=password,user=CRUDBaseUser(alias,email,password,Method,client.user.id))
    elif Method == Method.DELETE:
        client = Client.objects.get(id=GetElementFromRequest(request,'id'))
        user = User.objects.get(client=client)
        user.delete()
        client.delete()

def CRUDBaseUser(alias,email,password,Method,id=0):
    if Method == Method.INSERT:
        return User.objects.create_user(alias,email,password)
    elif Method == Method.UPDATE:
        user = User.objects.get(id=id)
        return user.update(alias,email,password)