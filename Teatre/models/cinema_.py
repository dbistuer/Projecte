from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Model


class Cinema(Model):
    adress = models.CharField(max_length=100)
    name = models.CharField(max_length=50)


class Room(Model):
    capacity = models.IntegerField(default=50, validators=[MinValueValidator(50)])
    Cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    number = models.IntegerField()

    def str(self) -> str:
        return "cinemas:" + self.Cinema + " Room: " + self.number

    class Meta:
        unique_together = (("number", "Cinema"),)
