import unittest
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount

def testListAccounts():
    return listAccounts("001")

def testListAccountsForSecondAccount():
    return listAccountsForSecondAccount("001")

class TestingAccountsAreCorrect(unittest.TestCase):
    def test_John_first_account(self):
        self.assertEqual(testListAccounts(), ['001', '9264945', 'Cheque', '500.90'], "Should be ['001', '9264945', 'Cheque', '500.90']")

    def test_John_second_account(self):
        self.assertEqual(testListAccountsForSecondAccount(), ['001', '7814135', 'Saving', '200.09'], "Should be ['001', '7814135', 'Saving', '200.09']")


if __name__ == '__main__':
    unittest.main()