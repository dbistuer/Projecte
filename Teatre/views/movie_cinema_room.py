from django.shortcuts import render

from Teatre.models import *
from django.contrib.auth.decorators import login_required


@login_required
def AddMovieCinemaRoom(request):
    user = request.user
    cinemas = Cinema.objects.all()
    movies = Movie.objects.all()
    rooms = Room.objects.all()
    client = Client.objects.get(user=user)
    messages = []

    if request.method == 'POST':
        movie_cinema_room = MovieCinemaRoom.objects.create()

        movie_cinema_room.date_movie = request.POST['date_movie']
        movie_cinema_room.Movie = Movie.objects.get(id=request.POST['movie'])
        movie_cinema_room.Room = Room.objects.get(id=request.POST['room'])
        movie_cinema_room.Cinema = Cinema.objects.get(id=request.POST['cinema'])

        movie_cinema_room.save()
        messages.append("Added successfully")


    json = {'client': client,
            'cinemas': cinemas,
            'movies': movies,
            'rooms': rooms,
            'messages': messages}
    return render(request, 'MovieCinemaRoom/add.html', json)
