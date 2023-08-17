import unittest
from ATM_Exam.src.main.filehandler.ReadUserInfo import listAccountsID


class TestingReadUserInfo(unittest.TestCase):
    def test_ListAccountsID(self):
        accountIndex = listAccountsID("../../../data/UserInfo.txt", "001")
        print(len(accountIndex))
        print(accountIndex.count("001"))
        print(accountIndex)


if __name__ == '__main__':
    unittest.main()