import csv
import os


def testingOpeningEx(filepath, removeDeL):
    with open('C:\\Users\\Hayden\\PycharmProjects\\DataAcademyATMExam\\ATM_Exam\\src\\main\\filehandler\\data\\' + filepath, 'r') as f:
        accountFile = [item for item in csv.reader((line.replace(removeDeL, "|") for line in f), delimiter='|')]
        return accountFile

#print(testingOpeningEx("OpeningAccountsData.txt", "|||"))

'''
# Future referance
with open(cwd + "\\" + filepath, 'r') as f:
'''

#not in use