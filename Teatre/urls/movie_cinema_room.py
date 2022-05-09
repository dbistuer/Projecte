from django.urls import path
from Teatre import views

urlpatterns_movie_cinema_room = [
    path('MovieCinemaRoom/Add', views.AddMovieCinemaRoom, name='add_movie_cinema_room'),
]
