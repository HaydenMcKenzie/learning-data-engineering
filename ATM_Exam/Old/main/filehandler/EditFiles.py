import csv

def removeDelimiter(filename, removeDeL):
    """
    :param filename: file name
    :param removeDeL: Identify delimiter
    :return: File without delimiters and creates rows into individual arrays
    """
    with open(filename, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace(removeDeL, "|") for line in file), delimiter='|')]
        return accountFile

def idsColumnOpenAccountData(filename):
    """
    :return: The first column in OpeningAccountData.txt
    """
    account = removeDelimiter(filename, "|||")
    ids = [row[0] for row in account]
    return ids

def firstColumnFromUserInfo(filename):
    """
    :return: Returns the first column of UserInfo.txt
    """
    account = removeDelimiter(filename, ",")
    ids = [row[3] for row in account]
    return ids