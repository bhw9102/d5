import unittest
import uuid

from .. import TicketProcessor
from .. import TicketUseCaseCreateCommand
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

    def test_(self):
        # Arrange
        # Action
        # Assertion
        pass



