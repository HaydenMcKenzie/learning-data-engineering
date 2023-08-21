from ATM_Exam.Old.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.Old.main.filehandler.EditFiles import idsColumnOpenAccountData



DATAPATH = "../../../data/OpeningAccountsData.txt"

def listAccountsOLD(filename, userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Depending on userID, removing ||| and retrieves first account from OpeningAccountsData.txt
    """
    account = removeDelimiter(filename, "|||")
    idIndex = idsColumnOpenAccountData(filename).index(userID)
    accountIndex = account[idIndex]
    return accountIndex

def listAccountsForSecondAccount(filename, userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Depending on userID, removing ||| and retrieves second account from OpeningAccountsData.txt
    """
    try:
        account = removeDelimiter(filename, "|||")
        idIndex = idsColumnOpenAccountData(filename).index(userID) + 1
        accountIndex = account[idIndex]
        return accountIndex
    except IndexError:
        pass