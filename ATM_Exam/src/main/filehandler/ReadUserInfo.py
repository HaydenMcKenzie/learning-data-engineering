from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter



def firstColumnFromUserInfo(DATAPATH):
    """
    :return: Returns the first column of UserInfo.txt
    """
    account = removeDelimiter(DATAPATH + "UserInfo.txt", ",")
    print(account)
    ids = [row[3] for row in account]
    print(ids)
    return ids


def listAccountsID(userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Depending on userID, it retrieves the first name, last name, phone number and user ID (Needs to match userID)
    """
    account = removeDelimiter("UserInfo.txt", ",")
    idIndex = firstColumnFromUserInfo().index(userID)
    accountIndex = account[idIndex]
    return accountIndex

