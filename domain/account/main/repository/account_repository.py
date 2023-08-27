import uuid

from ..entity.account import Account


class AccountRepository:
    def save(self, account: Account) -> Account:
        raise NotImplementedError()

    def get_by_primary_email(self, primary_email: str) -> Account:
        raise NotImplementedError()

    def exists_by_primary_email(self, primary_email: str) -> bool:
        raise NotImplementedError()
