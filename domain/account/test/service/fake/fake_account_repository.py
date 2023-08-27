from domain.account.main.entity.account import Account
from domain.account.main.repository.account_repository import AccountRepository


class FakeAccountRepository(AccountRepository):
    def __init__(self):
        self._key_map = dict()
        self._email_map = dict()

    def save(self, account: Account) -> Account:
        self._key_map[account.key] = account
        self._email_map[account.primary_email] = account
        return account

    def get_by_primary_email(self, primary_email: str) -> Account:
        return self._email_map[primary_email]

    def exists_by_primary_email(self, primary_email: str) -> bool:
        try:
            return bool(self._email_map[primary_email])
        except KeyError:
            return False

