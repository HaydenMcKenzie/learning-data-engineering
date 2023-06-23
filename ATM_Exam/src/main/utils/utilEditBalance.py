from ATM_Exam.src.main.commands.Balance import getBalance
from ATM_Exam.src.main.commands.Deposit import Add
from ATM_Exam.src.main.commands.Withdrawal import minus


def accountBalance(Option):
    """
    :param Option: User's ID
    :return: Prints Balance for select ID account
    """
    chequeOrSavings = input("")
    getBalance(chequeOrSavings, Option)


def accountAdd(Option):
    chequeOrSavings = input("")
    getBalance(chequeOrSavings, Option)

    # user input a float number
    userInputAddOrMinus = float(input())

    # print Add
    print(Add(chequeOrSavings, userInputAddOrMinus, Option))

accountAdd("001")

def accountMinus(Option):
    # select and print balance cheque or savings
    chequeOrSavings = input("")
    getBalance(chequeOrSavings, Option)

    # user input a float number
    userInputAddOrMinus = float(input())

    # print minus
    minus(chequeOrSavings, userInputAddOrMinus, Option)


def accountEditBalance(UserChoose, Option):
    if UserChoose == "1":
        accountAdd(Option)

    elif UserChoose == "2":
        accountMinus(Option)

    elif UserChoose == "3":
        accountBalance(Option)
