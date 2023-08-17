from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.src.main.filehandler.EditFiles import idsColumnOpenAccountData



DATAPATH = "../../../data/OpeningAccountData.txt"

def listAccounts(filename, userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Depending on userID, removing ||| and retrieves first account from OpeningAccountsData.txt
    """
    account = removeDelimiter(filename, "|||")
    idIndex = idsColumnOpenAccountData(DATAPATH).index(userID)
    accountIndex = account[idIndex]
    return accountIndex

def listAccountsForSecondAccount(DATAPATH, userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Depending on userID, removing ||| and retrieves second account from OpeningAccountsData.txt
    """
    try:
        account = removeDelimiter(DATAPATH + "OpeningAccountsData.txt", "|||")
        idIndex = idsColumnOpenAccountData(DATAPATH).index(userID) + 1
        accountIndex = account[idIndex]
        return accountIndex
    except IndexError:
        pass