from django.db import models
from django.db.models import Model


class MovieCinemaRoom(Model):
    Room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
    Cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, null=True)
    Movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)
    date_movie = models.DateField('date_movie', 'date_movie', null=True)

    def str(self) -> str:
        return "cinema:" + self.Cinema + " room: " + self.Room + " movie: " + self.Movie + " date_movie: " + str(
            self.date_movie)
