import unittest
from ATM_Exam.src.main.messages.AskingOption import answerOption

def testAnswerOptionOne():
    return answerOption("1")
def testAnswerOptionTwo():
    return answerOption("2")
def testAnswerOptionThree():
    return answerOption("3")

print("For answerOption (Input = 1):", testAnswerOptionOne())
print("For answerOption (Input = 2):", testAnswerOptionTwo())
print("For answerOption (Input = 3):", testAnswerOptionThree())



class testingAskingOption(unittest.TestCase):
    def test_AskingOption_One(self):
        self.assertEqual(testAnswerOptionOne(), "Which account do you wish to Deposit to:", "Should be Which account do you wish to Deposit to:")
    def test_AskingOption_Two(self):
            self.assertEqual(testAnswerOptionTwo(), "Which account do you wish to Withdraw from:", "Should be Which account do you wish to Withdraw from:")
    def test_AskingOption_Three(self):
        self.assertEqual(testAnswerOptionThree(), "Which account do you wish to see the Balance of:", "Which account do you wish to see the Balance of:")

if __name__ == '__main__':
    unittest.main()