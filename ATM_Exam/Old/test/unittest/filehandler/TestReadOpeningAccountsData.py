import unittest
from ATM_Exam.Old.main.filehandler.ReadOpeningAccountData import listAccounts


class TestingReadOpeningAccountData(unittest.TestCase):
    def test_ListAccounts(self):
        #Checking for the first account
        accountIndexFirstAccount = listAccounts("../../../../data/OpeningAccountsData.txt", "001", "|||", 0)
        firstAccountLength = len(accountIndexFirstAccount)
        checkingIndex = accountIndexFirstAccount.count("Saving")

        print(accountIndexFirstAccount)
        print(firstAccountLength)
        print(checkingIndex)

        # Checking for the Second account
        accountIndexSecondAccount = listAccounts("../../../../data/OpeningAccountsData.txt", "001", "|||", 1)
        secondAccountLength = len(accountIndexFirstAccount)
        checkingIndex = accountIndexSecondAccount.count("Cheque")

        print(accountIndexSecondAccount)
        print(secondAccountLength)
        print(checkingIndex)

if __name__ == '__main__':
    unittest.main()