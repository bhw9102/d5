from django.urls import path

from .controller.ticket_controller import get_tickets
from .controller.ticket_controller import TicketCreateController


urlpatterns = [
    path('', get_tickets, name='tickets'),
    path('create', TicketCreateController.as_view(), name='create-ticket'),
]