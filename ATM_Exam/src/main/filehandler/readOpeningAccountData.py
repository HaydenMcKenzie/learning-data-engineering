

from ATM_Exam.src.main.filehandler.editfiles import removeDelimiter
from ATM_Exam.src.main.filehandler.editfiles import idsColumnOpenAccountData




def listAccounts(userID):
    """
    :param userID: User Input
    :return: Depending on userID, removing ||| and retrieves first account from OpeningAccountsData.txt
    """
    account = removeDelimiter("OpeningAccountsData.txt", "|||")
    idIndex = idsColumnOpenAccountData().index(userID)
    accountIndex = account[idIndex]
    return accountIndex


def listAccountsForSecondAccount(userID):
    """
    :param userID: User Input
    :return: Depending on userID, removing ||| and retrieves second account from OpeningAccountsData.txt
    """
    try:
        account = removeDelimiter("OpeningAccountsData.txt", "|||")
        idIndex = idsColumnOpenAccountData().index(userID) + 1
        accountIndex = account[idIndex]
        return accountIndex
    except IndexError:
        pass
