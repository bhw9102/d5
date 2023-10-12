import uuid

from typing import Type
from typing import TypeVar

from domain.ticket.main.entity.ticket import Ticket
from domain.ticket.main.valueobject.ticket_status import TicketStatus

from django.db import models
from django.utils import timezone

from common.datetime import to_aware


T = TypeVar('T', bound='TicketDataModel')


class TicketDataModel(models.Model):
    key = models.UUIDField(primary_key=True)
    account_key = models.UUIDField()
    status = models.CharField()
    subject = models.TextField()
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=False)
    done_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'ticket_ticket'

    def to_entity(self) -> Ticket:
        return Ticket(
            key=self.key,
            account_key=self.account_key,
            status=TicketStatus(self.status),
            subject=self.subject,
            created_at=to_aware(self.created_at),
            updated_at=to_aware(self.updated_at),
            done_at=to_aware(self.done_at) if self.done_at is not None else None
        )

    @classmethod
    def of(
            cls: Type[T],
            ticket: Ticket
    ) -> T:
        return cls(
            key=ticket.key,
            account_key=ticket.account_key,
            status=ticket.status.value,
            subject=ticket.subject,
            created_at=ticket.created_at,
            updated_at=ticket.updated_at,
            done_at=ticket.done_at
        )
