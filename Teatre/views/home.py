from django.shortcuts import render
from Teatre.models import *

def home(request):
    return render(request,'home.html')