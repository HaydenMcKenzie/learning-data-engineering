import csv

'''
def readingFile(filepath):
    file = open(filepath, 'r')
    return file.read()
'''

'''
Function with inputs filepath and removeDel
Open and read filepath as file 
accountFile is a variable to replace removeDel with | with a delimiter of |
return accountFile
'''
def removeDelimiter(filepath, removeDeL):
    with open(filepath, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace(removeDeL, "|") for line in file), delimiter='|')]
        return accountFile


'''
Function firstColumn
account = removeDelimiter(filepath and removeDel)
ids = first row in account
return ids
'''
def firstColumn():
    account = removeDelimiter("./data/OpeningAccountsData.txt", "|||")
    ids = [row[0] for row in account]
    return ids
