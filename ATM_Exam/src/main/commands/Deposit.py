from ATM_Exam.src.main.commands.FloatToDollar import dollarAdd
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount

op1 = "1"
op2 = 100
op3 = "001"


def Add(Option, Input, UserID):
    if Option == "1":
        y = getAccount(UserID)[5]
        z = [float(y)]
        return dollarAdd(z[0], Input)
    elif Option == "2":
        y = getSecondAccount(UserID)[5]
        z = [float(y)]
        return dollarAdd(z[0], Input)
