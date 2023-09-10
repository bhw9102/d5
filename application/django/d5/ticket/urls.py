from django.urls import path

from .controller.ticket_controller import TicketController, get_tickets


urlpatterns = [
    path('', get_tickets, name='tickets'),
    path('create', TicketController.create_ticket, name='create-ticket'),
]