import uuid

from entity.account import Account


class AccountRepository:
    def save(self, account: Account) -> Account:
        return NotImplementedError()

    def get_by_primary_email(self, primary_email: str) -> Account:
        return NotImplementedError()