import uuid


class TicketUseCaseCreateCommand:
    def __init__(
            self,
            account_key: uuid.UUID,
            subject: str
    ):
        self.account_key = account_key
        self.subject = subject
