from .cinemas import urlpatterns_cinemas
from .movies import urlpatterns_movies
from .tickets import urlpatterns_tickets
from .movie_cinema_room import urlpatterns_movie_cinema_room
from Projecte.settings.base import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = urlpatterns_cinemas + urlpatterns_movies + urlpatterns_tickets + urlpatterns_movie_cinema_room + urlpatterns_tickets + static(MEDIA_URL, document_root=MEDIA_ROOT)
