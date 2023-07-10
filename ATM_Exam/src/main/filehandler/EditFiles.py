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

def idsColumnOpenAccountData(DATAPATH):
    """
    :return: The first column in OpeningAccountData.txt
    """
    account = removeDelimiter(DATAPATH + "OpeningAccountsData.txt", "|||")
    ids = [row[0] for row in account]
    return ids

