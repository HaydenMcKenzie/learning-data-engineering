import csv
from ATM_Exam.src.main.filehandler.editfiles import removeDelimiter

'''def removeDelimiter(filepath, removeDeL):
    with open(filepath, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace(removeDeL, "|") for line in file), delimiter='|')]
        return accountFile'''


def removeDelimiter2():
    account = removeDelimiter("UserInfo.txt", ",")
    ids = [row[3] for row in account]
    return ids


def listAccountsID(userID):
    account = removeDelimiter("UserInfo.txt", ",")
    idIndex = removeDelimiter2().index(userID)
    accountIndex = account[idIndex]
    return accountIndex




'''
For Future 
        choose = accountFile[0]
        choose1 = choose[0:2]
        name = " ".join(choose1)
print FirstName Surname
'''