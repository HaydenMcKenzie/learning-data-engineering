from ATM_Exam.src.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.src.main.filehandler.ReadUserInfo import firstColumnFromUserInfo

DATAPATH = "../../data/"
def gettingName(userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: based on userID, it receives first name and last name from UserInfo.txt and joins them
    """
    try:
        account = removeDelimiter(DATAPATH + "UserInfo.txt", ",")
        idIndex = firstColumnFromUserInfo(DATAPATH).index(userID)
        print(idIndex)
        accountIndex = account[idIndex]
        name = accountIndex[0:2]
        joinedName = " ".join(name)
        return joinedName
    except:
        pass
