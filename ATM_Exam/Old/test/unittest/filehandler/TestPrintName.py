import unittest
from ATM_Exam.Old.main.filehandler.PrintName import gettingName


class testingGettingName(unittest.TestCase):
    def test_GettingName(self):
        joinedName = gettingName("001")
        self.assertTrue(joinedName)
        print(joinedName)

if __name__ == '__main__':
    unittest.main()