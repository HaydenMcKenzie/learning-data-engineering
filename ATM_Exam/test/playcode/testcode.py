from ATM_Exam.src.main.commands.Balance import getBalance
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount
from ATM_Exam.src.main.commands.Deposit import Add
from ATM_Exam.src.main.commands.Withdrawal import minus


def accountBalance(userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Prints Balance for select ID account
    """
    chequeOrSavings = input("")
    getBalance(chequeOrSavings, userID)


def editNewBalanceForFile(userID, account, newbal):
    with open("C:\\Users\\Hayden\\PycharmProjects\\DataAcademyATMExam\\ATM_Exam\\src\\main\\filehandler\\data\\OpeningAccountsData.txt", 'r') as file:
        filedata = file.read()

    if account == "1":
        balance = getAccount(userID)[5]
        filedata = filedata.replace(balance, newbal)
    elif account == "2":
        balance = getSecondAccount(userID)[5]
        filedata = filedata.replace(balance, newbal)

    with open("C:\\Users\\Hayden\\PycharmProjects\\DataAcademyATMExam\\ATM_Exam\\src\\main\\filehandler\\data\\OpeningAccountsData.txt", "w") as file:
        file.write(filedata)


def accountAdd(userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Grabs balance and asks user for number and adds them. Returns new balance
    """
    chequeOrSavings = input("")
    getBalance(chequeOrSavings, userID)

    # user input a float number
    userInputAddOrMinus = float(input())

    # print Add
    newBalance = Add(chequeOrSavings, userInputAddOrMinus, userID)
    print("Your new balance is: $" + newBalance)
    editNewBalanceForFile(userID, chequeOrSavings, newBalance)



def accountMinus(userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Grabs balance and asks user for number and minuses them. Returns new balance
    """
    # select and print balance cheque or savings
    chequeOrSavings = input("")
    getBalance(chequeOrSavings, userID)

    # user input a float number
    userInputAddOrMinus = float(input())

    # print minus
    newBalance = minus(chequeOrSavings, userInputAddOrMinus, userID)

    try:
        if float(newBalance) > 0:
            editNewBalanceForFile(userID, chequeOrSavings, newBalance)
            print("Your new balance is: $" + newBalance)
        else:
            if chequeOrSavings == "1":
                print("Error - Wrong Input: Amount entered ($" + str(userInputAddOrMinus) + ") is greater than amount in account ($" + getAccount(userID)[5] + ")")
            elif chequeOrSavings == "2":
                print("Error - Wrong Input: Amount entered ($" + str(userInputAddOrMinus) + ") is greater than amount in account ($" + getSecondAccount(userID)[5] + ")")
    except ValueError:
        print("error")



def accountEditBalance(UserChoose, userID):
    """
    :param UserChoose: User input from ATM.py - Either 1, 2 or 3
    :param userID: User input from ATM.py - Either 001, 002 or 003
    :return: Adds/minuses for a new balance or grabs account balance
    """
    if UserChoose == "1":
        accountAdd(userID)

    elif UserChoose == "2":
        accountMinus(userID)

    elif UserChoose == "3":
        accountBalance(userID)