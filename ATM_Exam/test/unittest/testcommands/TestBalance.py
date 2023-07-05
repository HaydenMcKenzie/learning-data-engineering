import unittest
from ATM_Exam.src.main.commands.Balance import getBalance
from ATM_Exam.src.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.src.main.accounts.CreateAccount import deleteInfo

pushToFiles()
def testGetBalanceOne():
    return getBalance("1", "004")
def testGetBalanceTwo():
    return getBalance("2", "004")


class testingBalance(unittest.TestCase):
    def test_Balance_One(self):
        self.assertEqual(testGetBalanceOne(), None, "Should be The balance of 5739824 (Saving) is: $500.00")
    def test_Balance_Two(self):
        self.assertEqual(testGetBalanceTwo(), None, "Should be The balance of 5739824 (Saving) is: $500.00")
        deleteInfo()

if __name__ == '__main__':
    unittest.main()