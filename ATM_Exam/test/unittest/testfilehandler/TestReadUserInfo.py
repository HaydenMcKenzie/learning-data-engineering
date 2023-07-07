import unittest
from ATM_Exam.src.main.filehandler.ReadUserInfo import firstColumnFromUserInfo
from ATM_Exam.src.main.filehandler.ReadUserInfo import listAccountsID


class TestingReadUserInfo(unittest.TestCase):
    def test_FirstColumnFromUserInfo(self):
        self.assertEqual(testFirstColumnFromUserInfo(), ['AccountOwnerID', '001', '002', '003', '004'], "Should be ['AccountOwnerID', '001', '002', '003']")

    def test_ListAccountsID(self):
        self.assertEqual(testListAccountsID(), ['Hayden', 'McKenzie', '0422530222', '004'], "Should be ['Hayden', 'McKenzie', '0422530222', '004']")

if __name__ == '__main__':
    unittest.main()