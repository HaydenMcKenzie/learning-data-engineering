from ATM_Exam.src.main.accounts.AccountFunctions import getAccount
from ATM_Exam.src.main.accounts.AccountFunctions import getSecondAccount

'''
Gets John Smith's Cheque and Savings Details
'''


def johnFirstAccount():
    return getAccount("001")


def johnSecondAccount():
    return getSecondAccount("001")


'''
Gets Leanne Smith's Cheque and Savings Details
'''


def leanneFirstAccount():
    return getAccount("002")


def leanneSecondAccount():
    return getSecondAccount("002")


'''
Gets Kim Kash's Savings Details
'''


def kimOnlyAccount():
    return getAccount("003")

