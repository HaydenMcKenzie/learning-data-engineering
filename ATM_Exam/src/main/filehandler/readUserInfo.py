from ATM_Exam.src.main.filehandler.editfiles import removeDelimiter



def firstColumnFromUserInfo():
    """
    :return: Returns the first column of UserInfo.txt
    """
    account = removeDelimiter("UserInfo.txt", ",")
    ids = [row[3] for row in account]
    return ids


def listAccountsID(userID):
    """
    :param userID: User Input
    :return: Depending on userID, it retrieves the first name, last name, phone number and user ID (Needs to match userID)
    """
    account = removeDelimiter("UserInfo.txt", ",")
    idIndex = firstColumnFromUserInfo().index(userID)
    accountIndex = account[idIndex]
    return accountIndex

