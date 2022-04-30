from django.urls import path
from Teatre import views

urlpatterns_movies = [
    path('Movies/List', views.MovieList, name='list_movies'),
    path('Movies/Detail', views.MovieDetail, name='movie_detail'),
    path('Movies/Movie/<int:id>/<str:type>', views.Movie_, name='movie'),
    path('Movies/Movie/<int:id>', views.Movie_, name='movie_detail_'),
]
