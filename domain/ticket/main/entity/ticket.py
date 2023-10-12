import datetime
import uuid

from typing import Type
from typing import TypeVar
from typing import Optional

from ..valueobject.ticket_status import TicketStatus


T = TypeVar('T', bound='Ticket')


class Ticket:
    def __init__(
            self,
            key: uuid.UUID,
            account_key: uuid.UUID,
            status: TicketStatus,
            subject: str,
            created_at: datetime.datetime,
            updated_at: datetime.datetime,
            done_at: Optional[datetime.datetime]
    ):
        self.key = key
        self.account_key = account_key
        self.status = status
        self.subject = subject
        self.created_at = created_at
        self.updated_at = updated_at
        self.done_at = done_at

    # companion object
    @classmethod
    def create(
            cls: Type[T],
            key: uuid.UUID,
            account_key: uuid.UUID,
            subject: str
    ) -> T:
        now = datetime.datetime.now()
        return cls(
            key=key,
            account_key=account_key,
            status=TicketStatus.READY,
            subject=subject,
            created_at=now,
            updated_at=now,
            done_at=None
        )

    def done(self):
        now = datetime.datetime.now()
        self.status = TicketStatus.DONE
        self.done_at = now
        self.updated_at = now
