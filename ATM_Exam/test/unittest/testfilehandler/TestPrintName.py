import unittest
from ATM_Exam.src.main.filehandler.PrintName import gettingName
from ATM_Exam.src.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.src.main.accounts.CreateAccount import deleteInfo

pushToFiles()
def testGettingName():
    return gettingName("004")

print("For gettingName:", testGettingName())


class testingGettingName(unittest.TestCase):
    def test_GettingName(self):
        self.assertEqual(testGettingName(), "Hayden McKenzie", "Should be Hayden McKenzie")
        deleteInfo()

if __name__ == '__main__':
    unittest.main()