import datetime
import uuid

from zoneinfo import ZoneInfo
from typing import Type
from typing import TypeVar
from typing import Optional

from ..valueobject.ticket_status import TicketStatus


T = TypeVar('T', bound='Ticket')


class Ticket:
    def __init__(
            self,
            key: uuid.UUID,
            creator_key: uuid.UUID,
            assignee_key: Optional[uuid.UUID],
            status: TicketStatus,
            subject: str,
            created_at: datetime.datetime,
            updated_at: datetime.datetime,
            done_at: Optional[datetime.datetime]
    ):
        self.key = key
        self.creator_key = creator_key
        self.assignee_key = assignee_key
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
            creator_key: uuid.UUID,
            subject: str
    ) -> T:
        now = datetime.datetime.now(ZoneInfo('UTC'))
        return cls(
            key=key,
            creator_key=creator_key,
            assignee_key=creator_key,
            status=TicketStatus.READY,
            subject=subject,
            created_at=now,
            updated_at=now,
            done_at=None
        )

    def done(self):
        now = datetime.datetime.now(ZoneInfo('UTC'))
        self.status = TicketStatus.DONE
        self.done_at = now
        self.updated_at = now

    def assign(self, assignee_key: uuid.UUID):
        pass

