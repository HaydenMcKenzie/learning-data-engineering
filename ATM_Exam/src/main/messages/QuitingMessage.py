from ATM_Exam.src.main.filehandler.PrintName import gettingName
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount


def printingBalancesOfAccounts():
    """
    :return: An overall snapshot of all the accounts and balances
    """
    print("For " + gettingName("001") + ": ")
    print(getAccount("001")[4] + " (" + getAccount("001")[3] + ") balance is: $" + getAccount("001")[5])
    print(getSecondAccount("001")[4] + " (" + getSecondAccount("001")[3] + ") balance is: $" + getSecondAccount("001")[5] + "\n")
    print("For " + gettingName("002") + ": ")
    print(getAccount("002")[4] + " (" + getAccount("002")[3] + ") balance is: $" + getAccount("002")[5])
    print(getSecondAccount("002")[4] + " (" + getSecondAccount("002")[3] + ") balance is: $" + getSecondAccount("002")[5] + "\n")
    print("For " + gettingName("003") + ": ")
    print(getAccount("003")[4] + " (" + getAccount("003")[3] + ") balance is: $" + getAccount("003")[5])

