import unittest
import uuid

from domain.account.main.entity.account import Account


class AccountTest(unittest.TestCase):
    def test_계정을_생성합니다(self):
        # Arrange
        key = uuid.uuid4()
        primary_email = "bhw9102@gmail.com"
        password = "!Q@W#E$R"
        display_name = "배현우"

        # Action
        result = Account(
            key,
            primary_email,
            password,
            display_name
        )

        # Assertion
        self.assertEqual(result.key, key)
        self.assertEqual(result.primary_email, primary_email)
        self.assertEqual(result.password, password)
        self.assertEqual(result.display_name, display_name)


if __name__ == '__main__':
    unittest.main()
