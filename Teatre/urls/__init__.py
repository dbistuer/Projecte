from .cinemas import urlpatterns_cinemas
from .movies import urlpatterns_movies
from .tickets import urlpatterns_tickets
from Projecte.settings.base import MEDIA_ROOT,MEDIA_URL

urlpatterns =  urlpatterns_cinemas + urlpatterns_movies + urlpatterns_tickets