import uuid
from typing import List

from domain.ticket.main.entity.ticket import Ticket
from domain.ticket.main.repository.ticket_repository import TicketRepository

from ..models import TicketDataModel


class TicketRepositoryImpl(TicketRepository):
    def save(self, ticket: Ticket) -> Ticket:
        pass

    def find_all_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
        pass

    def get_by_key(self, key: uuid.UUID) -> Ticket:
        pass

