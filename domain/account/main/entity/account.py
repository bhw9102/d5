import uuid


class Account:
    def __init__(
            self,
            key: uuid.UUID,
            primary_email: str,
            password: str,
            display_name: str
    ):
        self.key = key
        self.primary_email = primary_email
        self.password = password
        self.display_name = display_name
