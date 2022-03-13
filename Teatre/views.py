from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/index.html',json)


def cinemaList(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/cinemaList.html',json)

def MovieDetail(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/MovieDetail.html',json)

def movieList(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/movieList.html',json)


def SignIn(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas': cinemas}
    return render(request, 'cinemas/SignIn.html', json)