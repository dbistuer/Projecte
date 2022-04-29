from .cinemas import urlpatterns_cinemas
from .movies import urlpatterns_movies
from .tickets import urlpatterns_tickets
from Projecte.settings.base import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = urlpatterns_cinemas + urlpatterns_movies + urlpatterns_tickets + static(MEDIA_URL, document_root=MEDIA_ROOT)
