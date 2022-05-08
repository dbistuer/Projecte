from django.urls import path
from Teatre import views

urlpatterns_cinemas = [
    path('Cinema/List', views.Cinema_List, name='list_cinemas'),
    path('Cinemas/Cinema/<int:id>/<str:type>', views.Cinema_, name='cinema_edit_delete'),
    path('Cinemas/Cinema/Edit/<int:id>', views.Cinema_Edit, name='cinema_edit'),
    path('Cinemas/Cinema/Delete/<int:id>', views.Cinema_, name='cinema_delete'),
    path('Cinemas/Cinema/<int:id>', views.Cinema_, name='cinema_detail'),
    path('Cinemas/New_Cinema',views.New_Cinema,name='new_cinema')
]
