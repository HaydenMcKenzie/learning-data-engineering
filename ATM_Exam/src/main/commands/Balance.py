from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount


def getBalance(Option, UserID):
    if Option == "1":
        print("The balance of " + getAccount(UserID)[3] + " (" + getAccount(UserID)[4] + ") is: $" + getAccount(UserID)[5])
    elif Option == "2":
        ifAccountIsThere = getSecondAccount(UserID)
        if ifAccountIsThere:
            print("The balance of " + getSecondAccount(UserID)[3] + " (" + getSecondAccount(UserID)[4] + ") is: $" + getSecondAccount(UserID)[5])

