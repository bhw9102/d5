import uuid

from ..entity.account import Account
from ..usecase.account_usecase import AccountUseCase
from ..repository.account_repository import AccountRepository
from ..exception.already_sign_up_primary_email_exception import AlreadySignUpPrimaryEmailException
from ..exception.illegal_password_exception import IllegalPasswordException


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
        if self._repository.exists_by_primary_email(primary_email):
            raise AlreadySignUpPrimaryEmailException()
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
        account = self._repository.get_by_primary_email(primary_email)
        if account.password != password:
            raise IllegalPasswordException()
        return account
