from enum import Enum
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Model
from .validators import DNIValidator, PhoneValidator, IBANValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Cinema(Model):
    adress = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

class Room(Model):
    capacity = models.IntegerField(default=50, validators=[MinValueValidator(50)])
    Cinema = models.ForeignKey(Cinema,on_delete=models.CASCADE)
    number = models.IntegerField()

    def str(self) -> str:
        return "cinemas:" + self.Cinema + " Room: " + self.number

    class Meta:
        unique_together = (("number", "Cinema"),)
    
class Client(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    adress = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, validators=[PhoneValidator])
    cardNumber = models.CharField(max_length=50, validators=[IBANValidator]) #TODO:revisar validacio de Numero de tarja
    DNI = models.CharField(max_length=9,validators=[DNIValidator],default='')

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Client.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

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
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("date", "Client", "Movie", "Room"),)

class Method(Enum):
    INSERT = 1
    UPDATE = 2
    DELETE = 3
