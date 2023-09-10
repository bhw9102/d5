
from domain.ticket.main.usecase.ticket_usecase import TicketUseCase

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from dependency_injector.wiring import inject
from dependency_injector.wiring import Provide

from ..container import TicketContainer
from ..forms.create_ticket_form import CreateTicketForm


@inject
def get_tickets(
        request: HttpRequest,
        ticket_use_case: TicketUseCase = Provide[TicketContainer.ticket_use_case]
) -> HttpResponse:
    if request.method != "GET":
        raise Exception()
    user = request.user
    if not user.is_authenticated:
        raise Exception()
    tickets = ticket_use_case.find_all_by_account_key(user.key)
    return render(request, 'tickets.html', dict(tickets=tickets))



class TicketController:
    @inject
    def __init__(
            self,
            ticket_use_case: TicketUseCase = Provide[TicketContainer.ticket_use_case]
    ):
        self._ticket_use_case = ticket_use_case

    def create_ticket(
            self,
            request: HttpRequest,
    ):
        if request.method == "GET":
            form = CreateTicketForm()
            return render(request, '', dict(form=form))

    def tickets(
            self,
            request: HttpRequest
    ):
        if request.method != "GET":
            raise Exception()
        user = request.user
        if not user.is_authenticated:
            raise Exception()
        self._ticket_use_case.find_all_by_account_key(user.key)


