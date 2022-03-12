from django.shortcuts import render
from .models import Cinema

# Create your views here.
def index(request):
    cinemas = Cinema.objects.all()
    json = {'cinemas':cinemas}
    return render(request,'cinemas/index.html',json)