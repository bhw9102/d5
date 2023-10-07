import uuid

from domain.ticket.main.usecase.ticket_usecase import TicketUseCase
from domain.ticket.main.contract.ticket_use_case_create_command import TicketUseCaseCreateCommand

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from dependency_injector.wiring import inject
from dependency_injector.wiring import Provide

from ..container import TicketContainer
from ..forms.create_ticket_form import CreateTicketForm


class TicketCreateController(View):
    @inject
    def __init__(
            self,
            ticket_use_case: TicketUseCase = Provide[TicketContainer.ticket_use_case],
            **kwargs
    ):
        self._ticket_use_case: TicketUseCase = ticket_use_case
        super().__init__(**kwargs)

    def get(self, request) -> HttpResponse:
        form = CreateTicketForm()
        return render(request, 'create_ticket.html', dict(form=form))

    def post(self, request) -> HttpResponse:
        form = CreateTicketForm(request.POST)
        user = request.user
        if not user:
            return redirect('index')
        if not request.user.is_authenticated:
            return redirect('index')
        if not form.is_valid():
            raise Exception()
        self._ticket_use_case.create(
            command=TicketUseCaseCreateCommand(
                account_key=user.key,
                subject=form.cleaned_data.get('subject')
            )
        )
        return redirect('tickets')


class TicketDoneController(View):
    @inject
    def __init__(
            self,
            ticket_use_case: TicketUseCase = Provide[TicketContainer.ticket_use_case],
            **kwargs
    ):
        self._ticket_use_case: TicketUseCase = ticket_use_case
        super().__init__(**kwargs)

    def post(self, request, key) -> HttpResponse:
        key = uuid.UUID(key)
        self._ticket_use_case.done(key)
        return redirect('tickets')


@inject
def get_tickets(
        request: HttpRequest,
        ticket_use_case: TicketUseCase = Provide[TicketContainer.ticket_use_case]
) -> HttpResponse:
    if request.method != "GET":
        raise Exception()
    user = request.user
    if not user.is_authenticated:
        return redirect('index')
    tickets = ticket_use_case.find_all_by_account_key(user.key)
    return render(request, 'tickets.html', dict(tickets=tickets))
