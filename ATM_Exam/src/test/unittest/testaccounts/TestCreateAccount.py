import unittest
from ATM_Exam.src.main.accounts.CreateAccount import create


def testCreate():
    account = create("Hayden", "McKenzie", "004", "4357289", "Saving", "100")
    return account


class testingCreateFunction(unittest.TestCase):
    # Testing create new account - testCreate returns is Fname = Hayden, Lname = McKenzie, ID = 004, accountType = Saving, accountNo = 4357289, value = 100
    def test_create_account(self):
        self.assertEqual(testCreate(), ['Hayden', 'McKenzie', '004', 'Saving', '4357289', '100'], "Should be ['Hayden', 'McKenzie', '004', 'Saving', '4357289', '100']")


if __name__ == '__main__':
    unittest.main()
