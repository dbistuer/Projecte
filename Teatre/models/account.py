from django.db import models
from django.db.models import Model
from Teatre.validators import DNIValidator, PhoneValidator, IBANValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, validators=[PhoneValidator])
    cardNumber = models.CharField(max_length=50, validators=[IBANValidator])
    DNI = models.CharField(max_length=9, validators=[DNIValidator], default='')

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Client.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
