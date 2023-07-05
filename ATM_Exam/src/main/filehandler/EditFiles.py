import csv


def removeDelimiter(filepath, removeDeL):
    """
    :param filepath: file name
    :param removeDeL: Identify delimiter
    :return: File without delimiters and creates rows into individual arrays
    """
    with open('C:\\Users\\Hayden\\PycharmProjects\\DataAcademyATMExam\\ATM_Exam\\src\\main\\filehandler\\data\\' + filepath, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace(removeDeL, "|") for line in file), delimiter='|')]
        return accountFile


def idsColumnOpenAccountData():
    """
    :return: The first column in OpeningAccountData.txt
    """
    account = removeDelimiter("OpeningAccountsData.txt", "|||")
    ids = [row[0] for row in account]
    return ids

