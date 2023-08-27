import uuid

from ..entity.account import Account
from ..usecase.account_usecase import AccountUseCase
from ..repository.account_repository import AccountRepository


class AccountProcessor(AccountUseCase):
    def __init__(
            self,
            repository: AccountRepository
    ):
        self._repository = repository

    def sign_up(
            self,
            primary_email: str,
            password: str,
            display_name: str
    ) -> Account:
        account = Account(
            uuid.uuid4(),
            primary_email,
            password,
            display_name
        )

        return self._repository.save(account)

    def sign_in(
            self,
            primary_email: str,
            password: str
    ) -> Account:
        pass