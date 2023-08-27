from ..entity.account import Account


class AccountUseCase:
    def sign_up(
            self,
            primary_email: str,
            password: str,
            display_name: str
    ):
        raise NotImplementedError()

    def sign_in(
            self,
            primary_email: str,
            password: str
    ):
        raise NotImplementedError()
