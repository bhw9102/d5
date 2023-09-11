from dependency_injector import containers
from dependency_injector import providers

from domain.ticket.main.service.ticket_service import TicketProcessor
from .repository.ticket_repository_impl import TicketRepositoryImpl


class TicketContainer(containers.DeclarativeContainer):
    ticket_use_case = providers.Factory(
        TicketProcessor,
        repository=TicketRepositoryImpl()
    )
