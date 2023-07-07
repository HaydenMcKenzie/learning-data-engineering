from ATM_Exam.src.main.commands.Balance import getBalance
from ATM_Exam.src.main.accounts.AccountUsers import getAccount
from ATM_Exam.src.main.accounts.AccountUsers import getSecondAccount
from ATM_Exam.src.main.commands.Deposit import Add
from ATM_Exam.src.main.commands.Withdrawal import minus
from ATM_Exam.src.main.messages.QuitingMessage import printingBalancesOfAccounts

def accountBalance(userID, chequeOrSavings):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :param chequeOrSavings: User Input from ATM.py - Either 1 or 2
    :return: Prints Balance for select ID account
    """
    if chequeOrSavings == "1" or chequeOrSavings == "2":
        if userID == "003" and chequeOrSavings != "1":
            print("Error - Wrong Input: Please enter valid option")
        else:
            getBalance(chequeOrSavings, userID)
    elif chequeOrSavings == "q":
        printingBalancesOfAccounts()
        quit()
    else:
        print("Error - Wrong Input: Please enter valid option")


def editNewBalanceForFile(userID, account, newBal):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :param account: User Input from ATM.py - Either 1 or 2
    :param newBal: New number - adding old balance with user input to make new balance
    :return: The balance (e.g. 500.90) changes to newBal
    """
    with open("../../../data/OpeningAccountsData.txt", 'r') as file:
        filedata = file.read()

    if account == "1":
        balance = getAccount(userID)[5]
        filedata = filedata.replace(balance, newBal)
    elif account == "2":
        balance = getSecondAccount(userID)[5]
        filedata = filedata.replace(balance, newBal)

    with open("../../../data/OpeningAccountsData.txt", "w") as file:
        file.write(filedata)


def accountAdd(userID, chequeOrSavings):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :param chequeOrSavings: User Input from ATM.py - Either 1 or 2
    :return: Grabs balance and asks user for number and adds them. Returns new balance
    """
    accountBalance(userID, chequeOrSavings)


    # user input a float number
    if chequeOrSavings == "1" or chequeOrSavings == "2":
        userInputAddOrMinus = input()
        if userInputAddOrMinus != "q":
            userInputAddOrMinus = float(userInputAddOrMinus)

            newBalance = Add(chequeOrSavings, userInputAddOrMinus, userID)
            print("Your new balance is: $" + newBalance)
            editNewBalanceForFile(userID, chequeOrSavings, newBalance)
        else:
            printingBalancesOfAccounts()
            quit()



def accountMinus(userID, chequeOrSavings):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :param chequeOrSavings: User Input from ATM.py - Either 1 or 2
    :return: Grabs balance and asks user for number and minuses them. Returns new balance
    """
    # select and print balance cheque or savings
    accountBalance(userID, chequeOrSavings)

    # user input a float number
    if chequeOrSavings == "1" or chequeOrSavings == "2":
        userInputAddOrMinus = input()
        if userInputAddOrMinus != "q":
            userInputAddOrMinus = float(userInputAddOrMinus)

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
                print("Error - Wrong Input: Amount entered ($" + str(userInputAddOrMinus) + ") is greater than amount in account ($" + getSecondAccount(userID)[5] + ")")


        else:
            printingBalancesOfAccounts()
            quit()




def accountEditBalance(UserChoose, userID, chequeOrSavings):
    """
    :param UserChoose: User input from ATM.py - Either 1, 2 or 3
    :param userID: User input from ATM.py - Either 001, 002 or 003
    :param chequeOrSavings: User Input from ATM.py - Either 1 or 2
    :return: Adds/minuses for a new balance or grabs account balance
    """
    if UserChoose == "1":
        accountAdd(userID, chequeOrSavings)

    elif UserChoose == "2":
        accountMinus(userID, chequeOrSavings)

    elif UserChoose == "3":
        accountBalance(userID, chequeOrSavings)

    elif UserChoose == "q":
        printingBalancesOfAccounts()
        quit()
    else:
        print("Error - Wrong Input: Please enter valid option")