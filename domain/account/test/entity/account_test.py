import os
import sys

current_file_path = os.path.abspath(__file__)
package_path = current_file_path.split("/d5/domain")[0]
sys.path.insert(0, f'{package_path}/d5/domain/account/main')


import unittest

from entity.account import Account


class AccountTest(unittest.TestCase):
    def test_something(self):
        for path in sys.path:
            print(path)
        self.assertEqual(True, False)  # add assertion here

    def test_계정을_생성합니다(self):
        result = Account(1, 2, 3, 4)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
