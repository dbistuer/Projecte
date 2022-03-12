from django.contrib import admin
from Teatre.models import Movie, Room, Client, Cinema, Ticket

# Register your models here.
admin.site.register(Movie)
admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Cinema)
admin.site.register(Ticket)
