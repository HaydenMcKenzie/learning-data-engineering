from ATM_Exam.src.main.utils.UtilAccountChoice import userAccountChoice
from ATM_Exam.src.main.utils.UtilEditBalance import accountEditBalance
from ATM_Exam.src.main.messages.AskingOption import askingOption
from ATM_Exam.src.main.messages.QuitingMessage import printingBalancesOfAccounts


def userInputStart(option):
    """
    :param option: User Input from mainProgram() - Either 001, 002, or 003
    :return: Prints first message with name that corresponds with the userID. If incorrect inputs, restart
    """
    try:
        if option != "q":
            askingOption(option) # Welcome jOin
        else:
            try:
                printingBalancesOfAccounts()
                quit()
            except TypeError:
                printingBalancesOfAccounts()
                quit()
    except TypeError:
        print("Error - Wrong Input: Please enter valid UserID")
        mainProgram()

def userEditAccount(userChoose, userID, chequeOrSavings):
    """
    :param userChoose: User Input from mainProgram() - Either 1, 2, or 3
    :param userID: User Input from mainProgram() - Either 001, 002, or 003
    :param chequeOrSavings: User Input from ATM.py - Either 1 or 2
    :return: Adding, minusing or checking balance of chosen account. If incorrect inputs, restart
    """
    try:
        accountEditBalance(userChoose, userID, chequeOrSavings)
    except TypeError:
        print("Error - Wrong Input: Please enter valid integer")
        mainProgram()
    except ValueError:
        print("Error - Wrong Input: Please enter valid integer")
        mainProgram()

def mainProgram():
    # select account
    Option = input("Please enter your UserID ")
    userInputStart(Option)

    # user input for chose of accounts
    UserChoose = input()
    userAccountChoice(UserChoose, Option)

    # Edit the account - add, minus or see balance
    chequeOrSavings = input()
    userEditAccount(UserChoose, Option, chequeOrSavings)

    # Restart program
    mainProgram()

# Call
mainProgram()