import unittest
from ATM_Exam.src.main.filehandler.readUserInfo import firstColumnFromUserInfo
from ATM_Exam.src.main.filehandler.readUserInfo import listAccountsID



def testFirstColumnFromUserInfo():
    return firstColumnFromUserInfo()

def testListAccountsID():
    return listAccountsID("001")


class TestingAccountsAreCorrect(unittest.TestCase):
    def test_FirstColumnFromUserInfo(self):
        self.assertEqual(testFirstColumnFromUserInfo(), ['AccountOwnerID', '001', '002', '003'], "Should be ['AccountOwnerID', '001', '002', '003']")

    def test_ListAccountsID(self):
        self.assertEqual(testListAccountsID(), ['John', 'Smith', '0403715629', '001'], "Should be ['John', 'Smith', '0403715629', '001']")


if __name__ == '__main__':
    unittest.main()