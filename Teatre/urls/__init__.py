from .cinemas import urlpatterns_cinemas
from .movies import urlpatterns_movies
from .tickets import urlpatterns_tickets
from .movie_cinema_room import urlpatterns_movie_cinema_room

urlpatterns = urlpatterns_cinemas + urlpatterns_movies + urlpatterns_tickets + urlpatterns_movie_cinema_room
