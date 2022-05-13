from django.urls import path
from Teatre import views

urlpatterns_tickets = [
    path('Ticket/List', views.ticket_list, name='list_tickets'),
    path('Ticket/select',views.ticket_select, name='select_tickets'),
    path('Ticket/Buy/<int:id_assignation>',views.ticket_buy, name='buy_ticket'),
    path('Ticket/Detail/<int:id_ticket>',views.ticket_detail,name='detail_ticket')
]