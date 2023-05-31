from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount
from ATM_Exam.src.main.commands.FloatToDollar import dollarAdd

op1 = "1"
op2 = 100
op3 = "001"


def Add(Option, Input, UserID):
    if Option == "1":
        y = listAccounts(UserID)[3]
        z = [float(y)]
        return dollarAdd(z[0], Input)
    elif Option == "2":
        y = listAccountsForSecondAccount(UserID)[3]
        z = [float(y)]
        return dollarAdd(z[0], Input)

