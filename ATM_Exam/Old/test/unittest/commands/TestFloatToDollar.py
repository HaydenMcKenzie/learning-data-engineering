import unittest
from ATM_Exam.Old.main.commands.FloatToDollar import dollarAdd
from ATM_Exam.Old.main.commands.FloatToDollar import dollarMinus

def testDollarAdd():
    return dollarAdd(100, 10)

def testDollarMinus():
    return dollarMinus(100, 10)

print("For testDollarAdd:", testDollarAdd())
print("For testDollarMinus:", testDollarMinus())


class testingWithdrawl(unittest.TestCase):
    def test_DollarAdd(self):
        self.assertEqual(testDollarAdd(), "110.00", "Should be 110")

    def test_DollarMinus(self):
        self.assertEqual(testDollarMinus(), "90.00", "Should be 90")

if __name__ == '__main__':
    unittest.main()