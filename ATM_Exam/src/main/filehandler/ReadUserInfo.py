from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.src.main.filehandler.EditFiles import firstColumnFromUserInfo

DATAPATH = "../../../data/UserInfo.txt"

def listAccountsID(filename, userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Depending on userID, it retrieves the first name, last name, phone number and user ID (Needs to match userID)
    """
    account = removeDelimiter(filename, ",")
    idIndex = firstColumnFromUserInfo(filename).index(userID)
    accountIndex = account[idIndex]
    return accountIndex
