from django.db import models
from django.db.models import Model
from .account import Client
from .cinema_ import Room


class Movie(Model):
    image = models.ImageField(upload_to='', null=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    duration = models.IntegerField()
    synopsis = models.CharField(max_length=500, default=' ')
    classification = models.CharField(default='X',max_length=10)

    def str(self):
        return "Id: %s Movie name: %s Genre: %s Movie duration: %s" % (self.id, self.name, self.genre, self.duration)


class Ticket(Model):
    date = models.DateTimeField(auto_now=True)
    price = models.FloatField(max_length=4)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("date", "Client", "Movie", "Room"),)
