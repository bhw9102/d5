import unittest
import uuid

from .. import TicketStatus
from .. import TicketProcessor
from .. import TicketUseCaseCreateCommand
from .. import DoesNotExistsTicketException
from .fake.fake_ticket_repository import FakeTicketRepository


class TicketProcessorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _repository = FakeTicketRepository()
        self.ticket_processor = TicketProcessor(_repository)

    def test_티켓을_작성_할_수_있다(self):
        # Arrange
        account_key = uuid.uuid4()
        subject = "티켓 작성 테스트"
        command = TicketUseCaseCreateCommand(
            account_key=account_key,
            subject=subject
        )

        # Action
        result = self.ticket_processor.create(command=command)

        # Assertion
        self.assertEqual(result.account_key, account_key)
        self.assertEqual(result.subject, subject)

    def test_티켓키로_티켓을_가져올_수_있다(self):
        # Arrange
        account_key = uuid.uuid4()
        subject = "티켓 작성 테스트"
        command = TicketUseCaseCreateCommand(
            account_key=account_key,
            subject=subject
        )
        ticket = self.ticket_processor.create(command=command)

        # Action
        result = self.ticket_processor.get_by_key(key=ticket.key)

        # Assertion
        self.assertEqual(result.key, ticket.key)
        self.assertEqual(result.account_key, ticket.account_key)
        self.assertEqual(result.subject, ticket.subject)

    def test_없는_티켓키로_티켓을_가져올_수_없다(self):
        # Arrange
        ticket_key = uuid.uuid4()

        # Action
        with self.assertRaises(DoesNotExistsTicketException) as error:
            self.ticket_processor.get_by_key(key=ticket_key)

        # Assertion
        self.assertEqual(
            error.exception.__class__,
            DoesNotExistsTicketException
        )

    def test_사용자가_작성한_티켓을_모두_가져올_수_있다(self):
        # Arrange
        account_key = uuid.uuid4()
        subject1 = "티켓 작성 테스트 1"
        command1 = TicketUseCaseCreateCommand(
            account_key=account_key,
            subject=subject1
        )
        self.ticket_processor.create(command=command1)
        subject2 = "티켓 작성 테스트 2"
        command2 = TicketUseCaseCreateCommand(
            account_key=account_key,
            subject=subject2
        )
        self.ticket_processor.create(command=command2)

        # Action
        result = self.ticket_processor.find_all_by_account_key(account_key=account_key)
        # Assertion
        self.assertEqual(len(result), 2)
        for ticket in result:
            self.assertEqual(ticket.account_key, account_key)

    def test_티켓을_완료할_수_있다(self):
        # Arrange
        account_key = uuid.uuid4()
        subject = "티켓 작성 테스트"
        command = TicketUseCaseCreateCommand(
            account_key=account_key,
            subject=subject
        )
        ticket = self.ticket_processor.create(command=command)

        # Action
        ticket = self.ticket_processor.done()

        # Assertion
        self.assertEqual(ticket.status, TicketStatus.DONE)

    def test_(self):
        # Arrange
        # Action
        # Assertion
        pass



