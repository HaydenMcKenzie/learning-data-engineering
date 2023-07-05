import unittest
from ATM_Exam.src.main.filehandler.ReadOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.ReadOpeningAccountData import listAccountsForSecondAccount
from ATM_Exam.src.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.src.main.accounts.CreateAccount import deleteInfo

pushToFiles()
def testListAccounts():
    return listAccounts("004")
def testListAccountsForSecondAccount():
    return listAccountsForSecondAccount("004")

print("For listAccounts:", testListAccounts())
print("For listAccountsForSecondAccount:", testListAccountsForSecondAccount())


class TestingReadOpeningAccountData(unittest.TestCase):
    def test_ListAccounts(self):
        self.assertEqual(testListAccounts(), ['004', '5739824', 'Saving', '500.00'], "Should be ['004', '5739824', 'Saving', '500.00']")

    def test_ListAccountsForSecondAccount(self):
        self.assertEqual(testListAccountsForSecondAccount(), ['004', '9771864', 'Cheque', '42.00'], "Should be ['004', '9771864', 'Cheque', '42.00']")
        deleteInfo()

if __name__ == '__main__':
    unittest.main()