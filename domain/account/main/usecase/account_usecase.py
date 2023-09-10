from abc import ABCMeta
from abc import abstractmethod
from ..entity.account import Account


class AccountUseCase(metaclass=ABCMeta):
    @abstractmethod
    def sign_up(
            self,
            primary_email: str,
            password: str,
            display_name: str
    ) -> Account:
        raise NotImplementedError()

    def sign_in(
            self,
            primary_email: str,
            password: str
    ) -> Account:
        raise NotImplementedError()
