from ATM_Exam.src.main.filehandler.data.ReadTheFiles import testingOpeningEx
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount
from ATM_Exam.src.main.messages.AskingOption import testingGettingChOrSav


#print(testingOpeningEx("OpeningAccountsData.txt", "|||"))

#UserID = input("Enter: ")
#testingGettingChOrSav(UserID)
#UserAnswer = input("Enter your chose: ")

def getBalance(Option, UserID):
    if Option == "1":
        print("The balance of " + listAccounts(UserID)[1] + " (" + listAccounts(UserID)[2] + ") is: $" + listAccounts(UserID)[3])
    elif Option == "2":
        print("The balance of " + listAccountsForSecondAccount(UserID)[1] + " (" + listAccountsForSecondAccount(UserID)[2] + ") is: $" + listAccountsForSecondAccount(UserID)[3])
    # else:
        # restart
