from django.urls import path
from Teatre import views

urlpatterns_cinemas = [
    path('Cinema/List', views.CinemaList, name='list_cinemas'),
    path('Cinema/Cinema/<int:id>/<str:type>', views.Cinema_, name='cinema_edit_delete'),
    path('Cinema/Cinema/Edit/<int:id>', views.Cinema_Edit, name='cinema_edit'),
    path('Cinema/Cinema/Delete/<int:id>', views.Cinema_Delete, name='cinema_delete'),
    path('Cinema/Cinema/<int:id>', views.Cinema_, name='cinema_detail'),
    path('Cinema/New_Cinema',views.New_Cinema,name='new_cinema'),
    path('Cinema/new_room', views.Create_sala, name='create_room'),
    path('Cinema/room_list/<int:id_cinema>', views.room_list, name='room_list'),
    path('Cinema/modify_room/<int:id_cinema>/<int:id_room>', views.modify_room, name='modify_room'),

]
