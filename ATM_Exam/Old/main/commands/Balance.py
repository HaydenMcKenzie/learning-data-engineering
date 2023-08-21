from ATM_Exam.Old.main.accounts.AccountUsers import getAccount
from ATM_Exam.Old.main.accounts.AccountUsers import getSecondAccount


def getBalance(option, UserID):
    """
    :param option: User Input from ATM.py - Either 1 or 2 (Cheque or Savings)
    :param UserID: User Input from ATM.py - Either 001, 002 or 003
    :return: From selected Option, it prints the balance of either Cheque or Savings
    """
    if option == "1":
        print("The balance of " + getAccount(UserID)[3] + " (" + getAccount(UserID)[4] + ") is: $" + getAccount(UserID)[5])
    elif option == "2":
        ifAccountIsThere = getSecondAccount(UserID)
        if ifAccountIsThere:
            print("The balance of " + getSecondAccount(UserID)[3] + " (" + getSecondAccount(UserID)[4] + ") is: $" + getSecondAccount(UserID)[5])

