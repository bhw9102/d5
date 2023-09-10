import uuid

from typing import List

from ..entity.ticket import Ticket
from ..repository.ticket_repository import TicketRepository
from ..usecase.ticket_usecase import TicketUseCase
from ..contract.ticket_use_case_create_command import TicketUseCaseCreateCommand


class TicketProcessor(TicketUseCase):
	def __init__(self, repository: TicketRepository):
		self._repository = repository

	def get_by_key(self, key: uuid.UUID) -> Ticket:
		return self._repository.get_by_key(key=key)

	def find_all_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
		return self._repository.find_all_by_account_key(account_key=account_key)

	def create(self, command: TicketUseCaseCreateCommand) -> Ticket:
		ticket = Ticket(
			key=uuid.uuid4(),
			account_key=command.account_key,
			subject=command.subject
		)
		return self._repository.save(ticket=ticket)
