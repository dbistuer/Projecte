from django.shortcuts import render
from .models import Cinema

# Create your views here.
def index(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/index.html',json)

def cinemaList(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/cinemaList.html',json)


def Login(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/Login.html',json)


def MovieDetail(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/MovieDetail.html',json)


def movieList(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/movieList.html',json)