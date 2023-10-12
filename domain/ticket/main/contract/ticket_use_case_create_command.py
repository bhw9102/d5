import uuid


class TicketUseCaseCreateCommand:
    def __init__(
            self,
            creator_key: uuid.UUID,
            subject: str
    ):
        self.creator_key = creator_key
        self.subject = subject
