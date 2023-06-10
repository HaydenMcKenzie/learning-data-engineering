from ATM_Exam.src.main.commands.FloatToDollar import dollarMinus
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount

def minus(Option, Input, UserID):
    if Option == "1":
        y = getAccount(UserID)[5]
        z = [float(y)]
        if z[0] - Input < 0:
            print("Error - Wrong Input: Amount entered ($" + str(Input) + ") is greater than amount in account ($" + y + ")")
        else:
            print(dollarMinus(z[0], Input))
    elif Option == "2":
        y = getSecondAccount(UserID)[5]
        z = [float(y)]
        if z[0] - Input < 0:
            print("Error - Wrong Input: Amount entered ($" + str(Input) + ") is greater than amount in account ($" + y + ")")
        else:
            print(dollarMinus(z[0], Input))


