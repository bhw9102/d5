import uuid
from typing import List

from domain.ticket.main.entity.ticket import Ticket
from domain.ticket.main.repository.ticket_repository import TicketRepository
from domain.ticket.main.exception.does_not_exists_ticket_exception import DoesNotExistsTicketException

from ..models import TicketDataModel


class TicketRepositoryImpl(TicketRepository):
    def save(self, ticket: Ticket) -> Ticket:
        ticket_data_model = TicketDataModel.of(ticket=ticket)
        ticket_data_model.save()
        return ticket_data_model.to_entity()

    def find_all_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
        return [item.to_entity() for item in TicketDataModel.objects.filter(account_key=account_key)]

    def get_by_key(self, key: uuid.UUID) -> Ticket:
        try:
            return TicketDataModel.objects.get(key=key).to_entity()
        except TicketDataModel.DoesNotExist:
            raise DoesNotExistsTicketException()

