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
		return self.repository.get_by_key(key=key)

	def find_all_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
		pass

	def create(self, command: TicketUseCaseCreateCommand) -> Ticket:
		ticket = Ticket(
			key=uuid.uuid4(),
			account_key=command.account_key,
			subject=command.subject
		)
		return self.repository.save(ticket=ticket)
