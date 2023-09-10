import uuid

from typing import Type
from typing import TypeVar

from domain.ticket.main.entity.ticket import Ticket
from domain.ticket.main.valueobject.ticket_status import TicketStatus

from django.db import models


T = TypeVar('T', bound='TicketDataModel')


class TicketDataModel(models.Model):
    key = models.UUIDField()
    account_key = models.UUIDField()
    status = models.CharField()
    subject = models.TextField()

    class Meta:
        db_table = 'ticket_ticket'

    def to_entity(self) -> Ticket:
        return Ticket(
            key=self.key,
            account_key=self.account_key,
            status=TicketStatus(self.status),
            subject=self.subject
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
            subject=ticket.subject
        )
