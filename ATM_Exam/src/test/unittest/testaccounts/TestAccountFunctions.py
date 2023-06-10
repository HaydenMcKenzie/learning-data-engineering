import unittest
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount

def testGetAccount():
    return getAccount("001")

def testGetSecondAccount():
    return getSecondAccount("003")


class testingAccountFunction(unittest.TestCase):
    # Test John's First account
    def test_getAccount_Function(self):
        self.assertEqual(testGetAccount(), ('John', 'Smith', '001', '9264945', 'Cheque', '500.90'), "Should be ('John', 'Smith', '001', '9264945', 'Cheque', '500.90')")

    # Test Kim's Second Account
    def test_getSecondAccount_Function(self):
        self.assertEqual(testGetSecondAccount(), None, "Should be None")


if __name__ == '__main__':
    unittest.main()
