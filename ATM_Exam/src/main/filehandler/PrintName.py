from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.src.main.filehandler.ReadUserInfo import firstColumnFromUserInfo

DATAPATH = "../../../data/UserInfo.txt"
def gettingName(userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: based on userID, it receives first name and last name from UserInfo.txt and joins them
    """
    account = removeDelimiter(DATAPATH, ",")
    print(account)
    idIndex = firstColumnFromUserInfo(DATAPATH).index(userID)
    print(idIndex)
    accountIndex = account[idIndex]
    print(accountIndex)
    name = accountIndex[0:2]
    print(name)
    joinedName = " ".join(name)
    print(joinedName)
    return joinedName

print(gettingName("001"))