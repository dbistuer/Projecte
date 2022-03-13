from django.core.validators import EmailValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Model
from django.core.validators import RegexValidator
from .validators import DNIValidator, PhoneValidator, IBANValidator

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
    telephone = models.CharField(max_length=15, validators=[PhoneValidator])
    cardNumber = models.CharField(max_length=50, validators=[IBANValidator]) #TODO:revisar validacio de Numero de tarja
    email = models.CharField(max_length=50,validators=[EmailValidator("Must be a valid email")])
    DNI = models.CharField(max_length=9,validators=[DNIValidator],default='')
    alias = models.CharField(max_length=20,unique=True,default='')
    password = models.CharField(max_length=20,default='')

    def str(self) -> str:
        return self.name

class Movie(Model):
    name = models.CharField(max_length=50)
    genere = models.CharField(max_length=50)
    duration = models.IntegerField()
    descripton = models.CharField(max_length=500, default=' ')

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