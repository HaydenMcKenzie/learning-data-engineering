import unittest
from ATM_Exam.src.main.commands.Withdrawal import minus

def testMinus():
    return minus("1", 100, "001")


class testingWithdrawl(unittest.TestCase):
    def test_Withdrawal_Function(self):
        self.assertEqual(testMinus(), None, "Should be $400.90")


if __name__ == '__main__':
    unittest.main()