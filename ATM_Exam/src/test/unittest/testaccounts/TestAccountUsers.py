import unittest
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount


def testFirstAccount():
    return getAccount("001")

def testSecondAccount():
    return getSecondAccount("001")




class testingCreateFunction(unittest.TestCase):
    def test_create_account(self):
        self.assertEqual(testFirstAccount(), ('John', 'Smith', '001', '9264945', 'Cheque', '500.90'), "Should be ('John', 'Smith', '001', '9264945', 'Cheque', '500.90')")


if __name__ == '__main__':
    unittest.main()