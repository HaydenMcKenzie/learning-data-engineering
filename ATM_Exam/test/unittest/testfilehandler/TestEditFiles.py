import unittest
from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.src.main.filehandler.EditFiles import idsColumnOpenAccountData
from ATM_Exam.src.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.src.main.accounts.CreateAccount import deleteInfo

class EditFilesTest(unittest.TestCase):

    def test_removeDelimiter(self):
        myresults = removeDelimiter("../../../data/UserInfo.txt",",")

        print(myresults)

if __name__ == '__main__':
    unittest.main()

