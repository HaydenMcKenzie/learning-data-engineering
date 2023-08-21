from ATM_Exam.Old.main.commands.FloatToDollar import dollarMinus
from ATM_Exam.Old.main.accounts.AccountUsers import getAccount
from ATM_Exam.Old.main.accounts.AccountUsers import getSecondAccount

def minus(Option, Input, UserID):
    """
    :param Option: User Input from ATM.py - Either 1 or 2
    :param Input: User Input from ATM.py - Number that will be minused from the balance
    :param UserID: User Input from ATM.py - Either 001, 002 or 003
    :return: Minus the balance of the account and the Input and returns new balance
    """
    if Option == "1":
        accountToInt = getAccount(UserID)[5]
        accountToFloat = [float(accountToInt)]
        return dollarMinus(accountToFloat[0], Input)
    elif Option == "2":
        accountToInt = getSecondAccount(UserID)[5]
        accountToFloat = [float(accountToInt)]
        return dollarMinus(accountToFloat[0], Input)

