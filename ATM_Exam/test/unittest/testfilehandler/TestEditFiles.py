import unittest
from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.src.main.filehandler.EditFiles import idsColumnOpenAccountData
from ATM_Exam.src.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.src.main.accounts.CreateAccount import deleteInfo

pushToFiles()
def testRemoveDelimiterOne():
    return removeDelimiter("OpeningAccountsData.txt", "|||")[6]
def testRemoveDelimiterTwo():
    return removeDelimiter("OpeningAccountsData.txt", "|||")[7]
def testIdsColumnOpenAccountData():
    return idsColumnOpenAccountData()

print("For removeDelimiter (First Account):", testRemoveDelimiterOne())
print("For removeDelimiter (Second Account):", testRemoveDelimiterTwo())
print("For idsColumnOpenAccountData:", testIdsColumnOpenAccountData())


class TestingRemoveDelimiter(unittest.TestCase):
    def test_RemoveDelimiter_One(self):
        self.assertEqual(testRemoveDelimiterOne(), ['004', '5739824', 'Saving', '500.00'], "Should be ['004', '5739824', 'Saving', '500.00']")

    def test_RemoveDelimiter_Two(self):
        self.assertEqual(testRemoveDelimiterTwo(), ['004', '9771864', 'Cheque', '42.00'], "Should be ['004', '9771864', 'Cheque', '42.00']")
    def test_idsColumnOpenAccountData(self):
        self.assertEqual(testIdsColumnOpenAccountData(), ['AccountOwnerID', '001', '001', '002', '002', '003', '004', '004'], "Should be ['AccountOwnerID', '001', '001', '002', '002', '003', '004', '004']")
        deleteInfo()

if __name__ == '__main__':
    unittest.main()