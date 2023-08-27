import unittest


from domain.account.main.entity.account import Account
from domain.account.main.usecase.account_usecase import AccountUseCase
from domain.account.main.service.account_processor import AccountProcessor
from domain.account.main.repository.account_repository import AccountRepository
from domain.account.main.exception.already_sign_up_primary_email_exception import AlreadySignUpPrimaryEmailException

from fake.fake_account_repository import FakeAccountRepository


class AccountProcessorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        repository = FakeAccountRepository()
        self.account_processor = AccountProcessor(repository)

    def test_회원가입을_할_수_있다(self):
        # Arrange
        primary_email = "bhw9102@gmail.com"
        password = "!Q@W#E$R"
        display_name = "배현우"

        # Action
        result = self.account_processor.sign_up(primary_email, password, display_name)

        # Assertion
        self.assertEqual(result.primary_email, primary_email)
        self.assertEqual(result.password, password)
        self.assertEqual(result.display_name, display_name)

    def test_이미_가입된_이메일로_회원가입을_할_수_없다(self):
        # Arrange
        primary_email = "bhw9102@gmail.com"
        password = "!Q@W#E$R"
        display_name = "배현우"
        self.account_processor.sign_up(primary_email, password, display_name)

        with self.assertRaises(AlreadySignUpPrimaryEmailException) as error:
            self.account_processor.sign_up(primary_email, password, display_name)

        # Action & Assertion
        self.assertEqual(
            error.exception.__class__,
            AlreadySignUpPrimaryEmailException
        )
