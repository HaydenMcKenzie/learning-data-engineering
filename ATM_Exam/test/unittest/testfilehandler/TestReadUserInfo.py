import unittest
from ATM_Exam.src.main.filehandler.ReadUserInfo import firstColumnFromUserInfo
from ATM_Exam.src.main.filehandler.ReadUserInfo import listAccountsID
from ATM_Exam.src.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.src.main.accounts.CreateAccount import deleteInfo

pushToFiles()
def testFirstColumnFromUserInfo():
    return firstColumnFromUserInfo()
def testListAccountsID():
    return listAccountsID("004")

print("For firstColumnFromUserInfo", testFirstColumnFromUserInfo())
print("For listAccountsID:", testListAccountsID())

class TestingReadUserInfo(unittest.TestCase):
    def test_FirstColumnFromUserInfo(self):
        self.assertEqual(testFirstColumnFromUserInfo(), ['AccountOwnerID', '001', '002', '003', '004'], "Should be ['AccountOwnerID', '001', '002', '003']")

    def test_ListAccountsID(self):
        self.assertEqual(testListAccountsID(), ['Hayden', 'McKenzie', '0422530222', '004'], "Should be ['Hayden', 'McKenzie', '0422530222', '004']")
        deleteInfo()

if __name__ == '__main__':
    unittest.main()