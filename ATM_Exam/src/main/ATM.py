from ATM_Exam.src.main.utils.utilAccountId import userAccountID
from ATM_Exam.src.main.utils.utilAccountChoice import userAccountChoice
from ATM_Exam.src.main.commands.Balance import getBalance
from ATM_Exam.src.main.commands.Deposit import Add
from ATM_Exam.src.main.commands.Withdrawal import minus


def start():
    # select account
    Option = input("Please enter your UserID ")
    userAccountID(Option)

    # user input for chose of accounts
    UserChoose = input()
    userAccountChoice(UserChoose, Option)

    try:
        if UserChoose == "1":
            try:
                # select and print balance cheque or savings
                chequeOrSavings = input("")
                getBalance(chequeOrSavings, Option)

                # user input a float number
                userInputAddOrMinus = float(input("Enter Number "))

                # print Add
                print(Add(chequeOrSavings, userInputAddOrMinus, Option))
            except ValueError:
                start()
        elif UserChoose == "2":
            try:
                # select and print balance cheque or savings
                chequeOrSavings = input("")
                getBalance(chequeOrSavings, Option)

                # user input a float number
                userInputAddOrMinus = float(input("Enter Number "))

                # print minus
                minus(chequeOrSavings, userInputAddOrMinus, Option)
            except ValueError:
                start()
        elif UserChoose == "3":
            chequeOrSavings = input("")
            getBalance(chequeOrSavings, Option)
    except TypeError:
        start()

    # Restart program
    start()


start()
