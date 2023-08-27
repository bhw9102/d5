import unittest


from domain.account.main.entity.account import Account
from domain.account.main.usecase.account_usecase import AccountUseCase
from domain.account.main.service.account_processor import AccountProcessor
from domain.account.main.repository.account_repository import AccountRepository

from fake.fake_account_repository import FakeAccountRepository


class AccountProcessorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        repository = FakeAccountRepository()
        self.account_processor = AccountProcessor(repository)

    def test_회원가입을_할_수_있다(self):
        primary_email = "bhw9102@gmail.com"
        password = "!Q@W#E$R"
        display_name = "배현우"

        result = self.account_processor.sign_up(primary_email, password, display_name)

        self.assertEqual(result.primary_email, primary_email)
        self.assertEqual(result.password, password)
        self.assertEqual(result.display_name, display_name)