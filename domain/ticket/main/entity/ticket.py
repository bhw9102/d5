import uuid

from ..valueobject.ticket_status import TicketStatus


class Ticket:
    def __init__(
          self,
          key: uuid.UUID,
          account_key: uuid.UUID,
          subject: str
    ):
        self.key = key
        self.account_key = account_key
        self.status = TicketStatus.READY
        self.subject = subject
