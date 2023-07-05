from ATM_Exam.src.main.filehandler.ReadUserInfo import listAccountsID
from ATM_Exam.src.main.filehandler.ReadOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.ReadOpeningAccountData import listAccountsForSecondAccount


def getAccount(accountID):
    """
    :param accountID: User Input
    :return: Retrieves the first account data
    """
    return listAccountsID(accountID)[0], listAccountsID(accountID)[1], listAccounts(accountID)[0], \
           listAccounts(accountID)[1], listAccounts(accountID)[2], listAccounts(accountID)[3]


def getSecondAccount(accountID):
    """
    :param accountID: User input
    :return: If there is a second account, it retrieves the second account data
    """
    ifAccountIsThere = listAccountsForSecondAccount(accountID)
    if ifAccountIsThere:
        return listAccountsID(accountID)[0], listAccountsID(accountID)[1], listAccountsForSecondAccount(accountID)[0], \
               listAccountsForSecondAccount(accountID)[1], listAccountsForSecondAccount(accountID)[2], \
               listAccountsForSecondAccount(accountID)[3]


def printAccountOptions(UserID):
    """
    :param UserID: User input
    :return: Depending on UserID, it prints 1 or both accounts.
    """
    print("1 for", getAccount(UserID)[3], "(" + getAccount(UserID)[4] + ")")
    ifAccountIsThere = getSecondAccount(UserID)
    if ifAccountIsThere:
        print("2 for", getSecondAccount(UserID)[3], "(" + getSecondAccount(UserID)[4] + ")")
