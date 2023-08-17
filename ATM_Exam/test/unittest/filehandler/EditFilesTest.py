import unittest
from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        accountFile = removeDelimiter("../../../data/OpeningAccountsData.txt", "|||")
        print(accountFile.count(self))


if __name__ == '__main__':
    unittest.main()
