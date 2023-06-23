import unittest
from ATM_Exam.src.main.commands.Deposit import Add

def testAdd():
    return Add("1", 100, "001")


class testingDeposit(unittest.TestCase):
    def test_Deposit_Function(self):
        self.assertEqual(testAdd(), "$600.90", "Should be $600.90")


if __name__ == '__main__':
    unittest.main()