import unittest
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount
from ATM_Exam.src.main.accounts.CreateAccount import pushToFiles
from ATM_Exam.src.main.accounts.CreateAccount import deleteInfo

pushToFiles()

def testFirstAccount():
    return getAccount("004")
def testSecondAccount():
    return getSecondAccount("004")

print("For getAccount:", testFirstAccount())
print("For getSecondAccount:", testSecondAccount())


class testingAccountsUsers(unittest.TestCase):
    def test_GetAccount(self):
        self.assertEqual(testFirstAccount(), ('Hayden', 'McKenzie', '004', '5739824', 'Saving', '500.00'), "Should be ('Hayden', 'McKenzie', '004', '5739824', 'Saving', '500.00')")
    def test_GetSecondAccount(self):
        self.assertEqual(testSecondAccount(), ('Hayden', 'McKenzie', '004', '9771864', 'Cheque', '42.00'), "Should be ('Hayden', 'McKenzie', '004', '9771864', 'Cheque', '42.00')")
        deleteInfo()


if __name__ == '__main__':
    unittest.main()