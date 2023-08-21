import unittest
from ATM_Exam.Old.main.commands.Deposit import Add
from ATM_Exam.Old.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.Old.main.accounts.CreateAccount import deleteInfo

pushToFiles()
def testAdd():
    return Add("1", 100, "004")

print("For testAdd:", testAdd())


class testingDeposit(unittest.TestCase):
    def test_Deposit(self):
        self.assertEqual(testAdd(), "600.00", "Should be 600.00")
        deleteInfo()

if __name__ == '__main__':
    unittest.main()