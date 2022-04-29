from django.urls import path
from Teatre import views

urlpatterns_movies = [
    path('Movie/List', views.MovieList, name='list_movies'),
    path('Movie/Detail', views.MovieDetail, name='movie_detail'),
]
