import uuid

from typing import List


class TicketUseCase:
	def get_by_key(key: uuid.UUID) -> Ticket:
		raise NotImplementedError()
	def find_by_account_key(account_key: uuid.UUID) ->  List[Ticket]:
		raise NotImplementedError()
	def create(command) -> Ticket:
		raise NotImplementedError()
