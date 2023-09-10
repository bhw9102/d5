import uuid
from typing import List

from . import Ticket
from . import TicketRepository
from . import DoesNotExistsTicketException


class FakeTicketRepository(TicketRepository):
    def __init__(self):
        self._map = dict()

    def save(self, ticket: Ticket) -> Ticket:
        self._map[ticket.key] = ticket
        return self._map[ticket.key]

    def find_all_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
        return [item for item in self._map.values() if item['key'] == account_key]

    def get_by_key(self, key: uuid.UUID) -> Ticket:
        try:
            return self._map[key]
        except KeyError:
            raise DoesNotExistsTicketException()