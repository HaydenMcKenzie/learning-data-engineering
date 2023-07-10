import unittest
from ATM_Exam.src.main.filehandler.ReadUserInfo import firstColumnFromUserInfo
from ATM_Exam.src.main.filehandler.ReadUserInfo import listAccountsID


class TestingReadUserInfo(unittest.TestCase):
    def test_FirstColumnFromUserInfo(self):
        ids = firstColumnFromUserInfo("../../../data/")
        self.assertTrue(ids)
        print(ids)

    def test_ListAccountsID(self):
        accountIndex = listAccountsID("../../../data/", "001")
        self.assertTrue(accountIndex)
        print(accountIndex)

if __name__ == '__main__':
    unittest.main()