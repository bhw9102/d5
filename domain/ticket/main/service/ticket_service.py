import uuid

from typing import List

from repository.ticket_repository import TicketRepository
from usecase.ticket_usecase import TicketUseCase


class TicketProcessor: TicketUseCase
	def __init__(self, repository):
		self.repository = repository
	def get_by_key(self, key: uuid.UUID) -> Ticket:
		pass
	def find_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
		pass
	def create(self, command) -> Ticket:
		pass
	def done(self, key: uuid.UUID) -> Ticket:
		pass
