import uuid


class Ticket:
  def __init__(
    self,
    key: uuid.UUID,
    account_key: uuid.UUID,
    subject: str
  ):
    self.key = key
    self.account_key = account_key
    self.subject = subject
