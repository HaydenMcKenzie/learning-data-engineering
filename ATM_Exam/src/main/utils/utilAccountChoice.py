from ATM_Exam.src.main.messages.AskingOption import answerOption
from ATM_Exam.src.main.messages.AskingOption import GettingChOrSav


def userAccountChoice(input, Option):
    try:
        if input == "1":
            answerOption(input)
            GettingChOrSav(Option)
        elif input == "2":
            answerOption(input)
            GettingChOrSav(Option)
        elif input == "3":
            answerOption(input)
            GettingChOrSav(Option)
        elif input == "q":
            answerOption(input)
            GettingChOrSav(Option)
    except ValueError:
        userAccountChoice(input, Option) # Restart