import csv


def readingFile(filepath):
    file = open(filepath, 'r')
    return file.read()


def removeDelimiter(filepath, removeDeL):
    with open(filepath, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace(removeDeL, "|") for line in file), delimiter='|')]
        return accountFile


print(removeDelimiter("./data/UserInfo.txt", ","))

def removeDelimiter2():
    account = removeDelimiter("./data/UserInfo.txt", ",")
    ids = [row[3] for row in account]
    return ids

print(removeDelimiter2())

def listAccounts(userID):
    account = removeDelimiter("./data/UserInfo.txt", ",")
    idIndex = removeDelimiter2().index(userID)
    accountIndex = account[idIndex]
    name = accountIndex[0:2]
    joinedName = " ".join(name)
    return joinedName

print(listAccounts("001"))
print(listAccounts("002"))
print(listAccounts("003"))


'''
For Future 
        choose = accountFile[0]
        choose1 = choose[0:2]
        name = " ".join(choose1)
print FirstName Surname
'''