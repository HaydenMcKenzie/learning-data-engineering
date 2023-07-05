from ATM_Exam.src.main.commands.FloatToDollar import dollarAdd
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount



def Add(Option, Input, UserID):
    """
    :param Option: User Input from ATM.py - Either 1 or 2
    :param Input: User Input from ATM.py - Number that will be added to the balance
    :param UserID: User Input from ATM.py - Either 001, 002 or 003
    :return: Adds the balance of the account and the Input and returns new balance
    """
    if Option == "1":
        accountToInt = getAccount(UserID)[5]
        accountToFloat = [float(accountToInt)]
        return dollarAdd(accountToFloat[0], Input)
    elif Option == "2":
        accountToInt = getSecondAccount(UserID)[5]
        accountToFloat = [float(accountToInt)]
        return dollarAdd(accountToFloat[0], Input)


