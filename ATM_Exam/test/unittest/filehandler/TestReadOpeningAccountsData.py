import unittest
from ATM_Exam.src.main.filehandler.ReadOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.ReadOpeningAccountData import listAccountsForSecondAccount


class TestingReadOpeningAccountData(unittest.TestCase):
    def test_ListAccounts(self):
        accountIndex = listAccounts("../../../data/", "001")
        self.assertTrue(accountIndex)
        print(accountIndex)
    def test_ListAccountsForSecondAccount(self):
        accountIndex = listAccountsForSecondAccount("../../../data/", "001")
        self.assertTrue(accountIndex)
        print(accountIndex)

if __name__ == '__main__':
    unittest.main()