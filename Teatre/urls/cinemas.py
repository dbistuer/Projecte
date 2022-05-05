from django.urls import path
from Teatre import views

urlpatterns_cinemas = [
    path('Cinema/List', views.CinemaList, name='list_cinemas'),
    path('Cinema/new_room', views.Create_sala, name='create_room'),
    path('Cinema/room_list/<int:id_cinema>', views.room_list, name='room_list'),

]
