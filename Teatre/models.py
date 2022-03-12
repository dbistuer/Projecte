from django.core.validators import EmailValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Model
from django.core.validators import RegexValidator



class Cinema(Model):
    adress = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

class Room(Model):
    capacity = models.IntegerField(default=50, validators=[MinValueValidator(50)])
    idCinema = models.ForeignKey(Cinema,on_delete=models.CASCADE)
    number = models.IntegerField()

    def str(self) -> str:
        return "cinemas:" + self.idCinema + " Room: " + self.number

    class Meta:
        unique_together = (("number", "idCinema"),)

class Client(Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    cardNumber = models.CharField(max_length=50) #TODO:fer validacio de Numero de tarja
    email = models.CharField(max_length=50,validators=[EmailValidator("Must be a valid telephone")])

    def str(self) -> str:
        return self.name

class Movie(Model):
    name = models.CharField(max_length=50)
    genere = models.CharField(max_length=50)
    duration = models.IntegerField()

    def str(self):
        return "Id: %s Movie name: %s Genre: %s Movie duration: %s" % (self.id, self.name, self.genre, self.duration)

class Ticket(Model):
    date = models.DateTimeField(auto_now=True)
    price = models.FloatField(max_length=4)
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    idMovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    idRoom = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("date", "idClient", "idMovie", "idRoom"),)