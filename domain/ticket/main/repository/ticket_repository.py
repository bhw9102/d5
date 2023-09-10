import uuid

from abc import ABCMeta
from abc import abstractmethod
from typing import List

from ..entity.ticket import Ticket


class TicketRepository(metaclass=ABCMeta):
	@abstractmethod
	def save(self, ticket: Ticket) -> Ticket:
		raise NotImplementedError

	@abstractmethod
	def find_all_by_account_key(self, account_key: uuid.UUID) -> List[Ticket]:
		raise NotImplementedError

	@abstractmethod
	def get_by_key(self, key: uuid.UUID) -> Ticket:
		raise NotImplementedError
