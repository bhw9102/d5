import unittest
import uuid

from .. import Ticket
from .. import TicketStatus


class TicketTest(unittest.TestCase):
    def test_티켓을_처음_생성할_수_있다(self):
        # Arrange
        ticket_key = uuid.uuid4()
        account_key = uuid.uuid4()
        subject = "티켓을 생성합니다."

        # Action
        ticket = Ticket.create(
            key=ticket_key,
            creator_key=account_key,
            subject=subject
        )

        # Assertion
        self.assertEqual(ticket.key, ticket_key)
        self.assertEqual(ticket.creator_key, account_key)
        self.assertEqual(ticket.subject, subject)
        self.assertEqual(ticket.status, TicketStatus.READY)

    def test_티켓을_완료시킬_수_있다(self):
        # Arrange
        ticket = Ticket.create(
            key=uuid.uuid4(),
            creator_key=uuid.uuid4(),
            subject="티켓을 완료시킵니다."
        )
        # Action
        ticket.done()
        # Assertion
        self.assertEqual(ticket.status, TicketStatus.DONE)

    def test_티켓을_처음_생성하면_작성자가_작업자가_됩니다(self):
        # Arrange
        ticket_key = uuid.uuid4()
        account_key = uuid.uuid4()
        subject = "티켓을 생성합니다."

        # Action
        ticket = Ticket.create(
            key=ticket_key,
            creator_key=account_key,
            subject=subject
        )

        # Assertion
        self.assertEqual(ticket.key, ticket_key)
        self.assertEqual(ticket.creator_key, account_key)
        self.assertEqual(ticket.assignee_key, account_key)