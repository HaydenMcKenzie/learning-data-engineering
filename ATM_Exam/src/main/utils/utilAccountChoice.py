from ATM_Exam.src.main.messages.AskingOption import answerOption
from ATM_Exam.src.main.messages.AskingOption import testingGettingChOrSav


def userAccountChoice(input, Option):
    try:
        if input == "1":
            answerOption(input)
            testingGettingChOrSav(Option)
        elif input == "2":
            answerOption(input)
            testingGettingChOrSav(Option)
        elif input == "3":
            answerOption(input)
            testingGettingChOrSav(Option)
        elif input == "q":
            answerOption(input)
            testingGettingChOrSav(Option)
    except ValueError:
        userAccountChoice(input, Option) # Restart