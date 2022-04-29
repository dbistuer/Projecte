from .cinemas import urlpatterns_cinemas
from .movies import urlpatterns_movies
from .tickets import urlpatterns_tickets

urlpatterns =  urlpatterns_cinemas + urlpatterns_movies + urlpatterns_tickets