import uuid

from django.urls import path

from .controller.ticket_controller import get_tickets
from .controller.ticket_controller import TicketCreateController
from .controller.ticket_controller import TicketDoneController


urlpatterns = [
    path('', get_tickets, name='tickets'),
    path('create', TicketCreateController.as_view(), name='create-ticket'),
    path('<str:key>/done', TicketDoneController.as_view(), name='done-ticket'),
]