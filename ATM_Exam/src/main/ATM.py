from ATM_Exam.src.main.messages.AskingOption import answerOption
from ATM_Exam.src.main.messages.AskingOption import askingOption
from ATM_Exam.src.main.messages.AskingOption import testingGettingChOrSav
from ATM_Exam.src.main.commands.Balance import getBalance

Option = input("Please enter your UserID ")
askingOption(Option)

UserChoose = input()
answerOption(UserChoose)

testingGettingChOrSav(Option)

chequeOrSavings = input("Enter 1 or 2: ")
getBalance(chequeOrSavings, Option)