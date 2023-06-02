import unittest
from ATM_Exam.src.main.accounts.AccountUsers import johnFirstAccount

def testJohnFirstAccount():
    return johnFirstAccount()


class testingCreateFunction(unittest.TestCase):
    # Testing John's first account details
    def test_create_account(self):
        self.assertEqual(testJohnFirstAccount(), ('John', 'Smith', '001', '9264945', 'Cheque', '500.90'), "Should be ('John', 'Smith', '001', '9264945', 'Cheque', '500.90')")


if __name__ == '__main__':
    unittest.main()