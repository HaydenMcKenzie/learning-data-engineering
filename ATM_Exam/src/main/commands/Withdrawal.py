from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount
from ATM_Exam.src.main.commands.FloatToDollar import dollarMinus


def minus(Option, Input, UserID):
    if Option == "1":
        y = listAccounts(UserID)[3]
        z = [float(y)]
        if z[0] - Input < 0:
            print("Error - Wrong Input: Amount entered ($" + str(Input) + ") is greater than amount in account ($" + y + ")")
        else:
            print(dollarMinus(z[0], Input))
    elif Option == "2":
        y = listAccountsForSecondAccount(UserID)[3]
        z = [float(y)]
        if z[0] - Input < 0:
            print("Error - Wrong Input: Amount entered ($" + str(Input) + ") is greater than amount in account ($" + y + ")")
        else:
            print(dollarMinus(z[0], Input))

