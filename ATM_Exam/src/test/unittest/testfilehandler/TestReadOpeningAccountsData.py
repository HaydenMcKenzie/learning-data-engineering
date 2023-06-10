import unittest
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount



class TestingAccountsAreCorrect(unittest.TestCase):
    # Testing John Smith (001) for his first account
    def test_John_first_account(self):
        self.assertEqual(listAccounts("001"), ['001', '9264945', 'Cheque', '500.90'], "Should be ['001', '9264945', 'Cheque', '500.90']")

    # Testing John Smith (001) for his second account
    def test_John_second_account(self):
        self.assertEqual(listAccountsForSecondAccount("001"), ['001', '7814135', 'Saving', '200.09'], "Should be ['001', '7814135', 'Saving', '200.09']")

    # Testing Leanne Smith (002) for his first account
    def test_Leanne_first_account(self):
        self.assertEqual(listAccounts("002"), ['002', '9676422', 'Saving', '1200.00'], "Should be ['002', '9676422', 'Saving', '1200.00']")

    # Testing Leanne Smith (002) for his second account
    def test_Leanne_second_account(self):
        self.assertEqual(listAccountsForSecondAccount("002"), ['002', '7524155', 'Cheque', '50.00'], "Should be ['002', '7524155', 'Cheque', '50.00']")

    # Testing Kim Kash  (003) for his first account
    def test_Kim_first_account(self):
        self.assertEqual(listAccounts("003"), ['003', '9042221', 'Saving', '4000.20'], "Should be ['003', '9042221', 'Saving', '4000.20']")

    # Testing Kim Kash (003) for his second account
    def test_Kim_second_account(self):
        self.assertEqual(listAccountsForSecondAccount("003"), None, "Should be None")


class TestingAccountsArentCorrect(unittest.TestCase):
    # Testing John's first account doesn't have his second account values
    def test_John_First_Account_Is_Not_His_Second_Account(self):
        self.assertNotEqual(listAccounts("001"), ['001', '7814135', 'Saving', '200.09'], "Should be ['001', '9264945', 'Cheque', '500.90']")

    # Testing Kim's second account is not present
    def test_Kim_Second_Account_Is_Not_Present(self):
        self.assertNotEqual(listAccountsForSecondAccount("003"), ['003', '9042221', 'Saving', '4000.20'], "Should be None")

if __name__ == '__main__':
    unittest.main()