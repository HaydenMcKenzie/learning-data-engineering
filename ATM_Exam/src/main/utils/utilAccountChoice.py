from ATM_Exam.src.main.messages.AskingOption import answerOption
from ATM_Exam.src.main.accounts.AccountUsers import printAccountOptions

def userAccountChoice(input, Option):
    try:
        if input == "1":
            answerOption(input)
            printAccountOptions(Option)
        elif input == "2":
            answerOption(input)
            printAccountOptions(Option)
        elif input == "3":
            answerOption(input)
            printAccountOptions(Option)
        elif input == "q":
            answerOption(input)
            printAccountOptions(Option)
    except ValueError:
        userAccountChoice(input, Option)

userAccountChoice("1", "001")