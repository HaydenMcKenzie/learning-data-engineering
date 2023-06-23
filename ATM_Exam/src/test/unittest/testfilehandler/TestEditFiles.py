import unittest
from ATM_Exam.src.main.filehandler.editfiles import removeDelimiter


def testremoveDelimiter():
    return removeDelimiter("OpeningAccountsData.txt", "|||")




class TestingAccountsAreCorrect(unittest.TestCase):
    def test_John_first_account(self):
        self.assertEqual(testremoveDelimiter(), [['AccountOwnerID', 'AccountNumber', 'AccountType', 'OpeningBalance'], ['001', '9264945', 'Cheque', '500.90'], ['001', '7814135', 'Saving', '200.09'], ['002', '9676422', 'Saving', '1200.00'], ['002', '7524155', 'Cheque', '50.00'], ['003', '9042221', 'Saving', '4000.20']], "Should be [['AccountOwnerID', 'AccountNumber', 'AccountType', 'OpeningBalance'], ['001', '9264945', 'Cheque', '500.90'], ['001', '7814135', 'Saving', '200.09'], ['002', '9676422', 'Saving', '1200.00'], ['002', '7524155', 'Cheque', '50.00'], ['003', '9042221', 'Saving', '4000.20']]")


if __name__ == '__main__':
    unittest.main()