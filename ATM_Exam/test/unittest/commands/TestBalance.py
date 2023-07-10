import unittest
from ATM_Exam.src.main.commands.Balance import getBalance

class testingBalance(unittest.TestCase):
    def test_Balance_One(self):
        balance = getBalance("1", "001")
        self.assertTrue(balance)
        print(balance)

    def test_Balance_Two(self):
        self.assertEqual(testGetBalanceTwo(), None, "Should be The balance of 5739824 (Saving) is: $500.00")

if __name__ == '__main__':
    unittest.main()