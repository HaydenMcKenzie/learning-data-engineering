import csv


def removeDelimiter(filepath, removeDeL):
    with open('C:\\Users\\Hayden\\PycharmProjects\\DataAcademyATMExam\\ATM_Exam\\src\\main\\filehandler\\data\\' + filepath, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace(removeDeL, "|") for line in file), delimiter='|')]
        return accountFile

#print(removeDelimiter("OpeningAccountsData.txt", "|||"))


def idsColumnOpenAccountData():
    account = removeDelimiter("OpeningAccountsData.txt", "|||")
    ids = [row[0] for row in account]
    return ids


