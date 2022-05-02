from django.urls import path
from Teatre import views

urlpatterns_cinemas = [
    path('Cinema/List', views.CinemaList, name='list_cinemas'),
    path('Cinema/Detail', views.CinemaDetail, name='cinema_detail'),
]
