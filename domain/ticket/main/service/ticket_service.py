import uuid

from typing import List

from ..entity.ticket import Ticket
from ..repository.ticket_repository import TicketRepository
from ..usecase.ticket_usecase import TicketUseCase
from ..contract.ticket_use_case_create_command import TicketUseCaseCreateCommand


class TicketProcessor(TicketUseCase):
	def __init__(self, repository: TicketRepository):
		self.repository = repository

	def get_by_key(self, key: uuid.UUID) -> Ticket:
		pass

	def find_all_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
		pass

	def create(self, command: TicketUseCaseCreateCommand) -> Ticket:
		pass
