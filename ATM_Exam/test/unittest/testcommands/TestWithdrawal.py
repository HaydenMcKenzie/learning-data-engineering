import unittest
from ATM_Exam.src.main.commands.Withdrawal import minus
from ATM_Exam.src.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.src.main.accounts.CreateAccount import deleteInfo

pushToFiles()
def testMinusOne():
    return minus("1", 100, "004")
def testMinusTwo():
    return minus("2", 10, "004")

print("For minus (First Account):", testMinusOne())
print("For minus (Second Account):", testMinusTwo())

class testingWithdrawl(unittest.TestCase):
    def test_Withdrawal_One(self):
        self.assertEqual(testMinusOne(), "400.00", "Should be 400.00")

    def test_Withdrawal_Two(self):
        self.assertEqual(testMinusTwo(), "32.00", "Should be 32.00")
        deleteInfo()

if __name__ == '__main__':
    unittest.main()