import uuid

from typing import List

from entity.ticket import Ticket


class TicketRepository:
	def save(ticket: Ticket) -> Ticket:
		raise NotImplementedError
	def find_all_by_account_key(account_key: uuid.UUID) -> List[Ticket]:
		raise NotImplementedError
	def get_by_key(key: uuid.UUID) -> Ticket:
		raise NotImplementedError
