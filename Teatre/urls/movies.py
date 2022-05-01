from django.urls import path
from Teatre import views

urlpatterns_movies = [
    path('Movies/List', views.Movie_List, name='list_movies'),
    path('Movies/Movie/<int:id>/<str:type>', views.Movie_, name='movie_edit_delete'),
    path('Movies/Movie/Edit/<int:id>', views.Movie_Edit, name='movie_edit'),
    path('Movies/Movie/Delete/<int:id>', views.Movie_, name='movie_delete'),
    path('Movies/Movie/<int:id>', views.Movie_, name='movie_detail'),
    path('Movies/New_Movie',views.New_Movie,name='new_movie')
]
