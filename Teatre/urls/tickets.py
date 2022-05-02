from django.urls import path
from Teatre import views

urlpatterns_tickets = [
    path('Ticket/List', views.ticket_list, name='list_tickets'),
]
