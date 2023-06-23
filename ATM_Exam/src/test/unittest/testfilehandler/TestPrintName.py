import unittest
from ATM_Exam.src.main.filehandler.PrintName import gettingName

def testGettingName():
    return gettingName("001")


class testingDeposit(unittest.TestCase):
    def test_Deposit_Function(self):
        self.assertEqual(testGettingName(), "John Smith", "Should be John Smith")


if __name__ == '__main__':
    unittest.main()