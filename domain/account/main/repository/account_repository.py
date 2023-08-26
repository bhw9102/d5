import uuid

from entity.account import Account


class AccountRepository:
    def save(self, account: Account) -> Account:
        return NotImplementedError()

    def get_by_key(self, key: uuid.UUID) -> Account:
        return NotImplementedError()
