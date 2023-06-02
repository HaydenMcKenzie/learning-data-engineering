from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount



def getBalance(Option, UserID):
    if Option == "1":
        print("The balance of " + listAccounts(UserID)[1] + " (" + listAccounts(UserID)[2] + ") is: $" + listAccounts(UserID)[3])
    elif Option == "2":
        ifAccountIsThere = listAccountsForSecondAccount(UserID)
        if ifAccountIsThere:
            print("The balance of " + listAccountsForSecondAccount(UserID)[1] + " (" + listAccountsForSecondAccount(UserID)[2] + ") is: $" + listAccountsForSecondAccount(UserID)[3])

getBalance("1", "001")