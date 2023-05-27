from ATM_Exam.src.main.messages.AskingOption import answerOption
from ATM_Exam.src.main.messages.AskingOption import askingOption
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount

Option = input("Enter ID: ")
askingOption(Option)

UserChoose = input("Enter Chose: ")
answerOption(UserChoose)

def testingGettingChOrSav():
    print("1 for", listAccounts(Option)[1], "(" + listAccounts(Option)[2] + ")")
    ifAccountIsThere = listAccountsForSecondAccount(Option)
    if ifAccountIsThere:
        print("2 for", listAccountsForSecondAccount(Option)[1], "(" + listAccountsForSecondAccount(Option)[2] + ")")


# Not in use