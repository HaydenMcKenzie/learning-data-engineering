import unittest
from ATM_Exam.Old.main.accounts.CreateAccount import createForOpeningAccountsData
from ATM_Exam.Old.main.accounts.CreateAccount import createForUserInfo

def testCreateAccountOne():
    return createForOpeningAccountsData("004", "5739824", "Saving", "500.00")
def testCreateAccountTwo():
    return createForUserInfo("004", "9771864", "Cheque", "42.00")

print("For createForOpeningAccountsData:", testCreateAccountOne())
print("For createForUserInfo:", testCreateAccountTwo())



class testingCreateAccount(unittest.TestCase):
    def test_create_first_account(self):
        self.assertEqual(testCreateAccountOne(), "004|||5739824|||Saving|||500.00", "Should be 004|||5739824|||Saving|||500.00")

    def test_create_second_account(self):
        self.assertEqual(testCreateAccountTwo(), "004,9771864,Cheque,42.00", "Should be 004,9771864,Cheque,42.00")


if __name__ == '__main__':
    unittest.main()
