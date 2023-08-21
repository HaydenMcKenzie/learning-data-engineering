from ATM_Exam.Old.main.filehandler.EditFiles import removeDelimiter
from ATM_Exam.Old.main.filehandler.EditFiles import idsColumnOpenAccountData

DATAPATH = "../../../data/OpeningAccountsData.txt"

def listAccounts(filename, userID, delim, accountNo):
    account = removeDelimiter(filename, delim)
    idIndex = idsColumnOpenAccountData(filename).index(userID) + accountNo
    accountIndex = account[idIndex]
    return accountIndex