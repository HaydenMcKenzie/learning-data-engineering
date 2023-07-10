import unittest
from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.src.main.filehandler.EditFiles import idsColumnOpenAccountData

class EditFilesTest(unittest.TestCase):

    def test_removeDelimiter(self):
        accountFile = removeDelimiter("../../../data/UserInfo.txt",",")
        self.assertTrue(accountFile)
        print(accountFile)
    def test_idsColumnOpenAccountData(self):
        accountFile = idsColumnOpenAccountData("../../../data/")
        self.assertTrue(accountFile)
        print(accountFile)

if __name__ == '__main__':
    unittest.main()

