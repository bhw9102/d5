import uuid

from abc import ABCMeta
from abc import abstractmethod
from typing import List

from ..entity.ticket import Ticket
from ..contract.ticket_use_case_create_command import TicketUseCaseCreateCommand


class TicketUseCase(metaclass=ABCMeta):
	@abstractmethod
	def get_by_key(self, key: uuid.UUID) -> Ticket:
		raise NotImplementedError()

	@abstractmethod
	def find_all_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
		raise NotImplementedError()

	@abstractmethod
	def create(self, command: TicketUseCaseCreateCommand) -> Ticket:
		raise NotImplementedError()
