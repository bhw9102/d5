import unittest


from domain.account.main.entity.account import Account
from domain.account.main.usecase.account_usecase import AccountUseCase
from domain.account.main.service.account_processor import AccountProcessor
from domain.account.main.repository.account_repository import AccountRepository
from domain.account.main.exception.already_sign_up_primary_email_exception import AlreadySignUpPrimaryEmailException
from domain.account.main.exception.illegal_password_exception import IllegalPasswordException

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

        # Action
        with self.assertRaises(AlreadySignUpPrimaryEmailException) as error:
            self.account_processor.sign_up(primary_email, password, display_name)

        # Assertion
        self.assertEqual(
            error.exception.__class__,
            AlreadySignUpPrimaryEmailException
        )

    def test_이메일과_비밀번호를_입력해서_가입된_계정으로_로그인_할_수_있다(self):
        # Arrange
        primary_email = "bhw9102@gmail.com"
        password = "!Q@W#E$R"
        display_name = "배현우"
        self.account_processor.sign_up(primary_email, password, display_name)

        # Action
        result = self.account_processor.sign_in(primary_email, password)

        # Assertion
        self.assertEqual(result.primary_email, primary_email)
        self.assertEqual(result.password, password)
        self.assertEqual(result.display_name, display_name)

    def test_잘못된_비밀번호를_입력하면_로그인_할_수_없다(self):
        # Arrange
        primary_email = "bhw9102@gmail.com"
        password = "!Q@W#E$R"
        display_name = "배현우"
        error_password = "@W#E$R%T"
        self.account_processor.sign_up(primary_email, password, display_name)

        # Action
        with self.assertRaises(IllegalPasswordException) as error:
            self.account_processor.sign_in(primary_email, error_password)

        # Assertion
        self.assertEqual(
            error.exception.__class__,
            IllegalPasswordException
        )
