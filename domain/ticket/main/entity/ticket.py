import uuid

from typing import Type
from typing import TypeVar

from ..valueobject.ticket_status import TicketStatus


T = TypeVar('T', bound='Ticket')


class Ticket:
    def __init__(
            self,
            key: uuid.UUID,
            account_key: uuid.UUID,
            status: TicketStatus,
            subject: str
    ):
        self.key = key
        self.account_key = account_key
        self.status = status
        self.subject = subject

    # companion object
    @classmethod
    def create(
            cls: Type[T],
            key: uuid.UUID,
            account_key: uuid.UUID,
            subject: str
    ) -> T:
        return cls(
            key=key,
            account_key=account_key,
            status=TicketStatus.READY,
            subject=subject
        )

    def done(self):
        self.status = TicketStatus.DONE
