from entity.account import Account


class AccountUseCase:
    def sign_in_and_up(self, primary_email: str, password: str) -> Account: