from ATM_Exam.src.main.utils.utilAccountChoice import userAccountChoice
from ATM_Exam.src.main.utils.utilEditBalance import accountEditBalance
from ATM_Exam.src.main.messages.AskingOption import askingOption

def userInputStart(Option):
    """
    :param Option: User's input for id
    :return askingOption(Option): grabs user's name base on user id
    Validates that Options doesn't "q"
    If it is "q", it quits the program
    If Option doesn't = 001, 002 or 003, it recall mainProgram()
    """
    try:
        if Option != "q":
            askingOption(Option)
        else:
            try:
                quit()
            except TypeError:
                quit()
    except TypeError:
        mainProgram()

def userEditAccount(UserChoose, Option):
    """
    :param UserChoose: User's input for Deposit, Withdraw, Balance or Quit
    :param Option: User's input for id
    :return: Adding, minusing or checking balance of chosen account
    Makes sure that user inputs are int/floats. If not, recall mainProgram()
    """
    try:
        accountEditBalance(UserChoose, Option)
    except TypeError:
        mainProgram()
    except ValueError:
        mainProgram()

def mainProgram():
    """
    User input for id
    Print name and prompt user for deposit, withdraw, balance and quit
    User input for choice
    Print one or both of the selected ids accounts
    User input for number
    Print new balance or account balance
    Recall mainProgram()
    """
    # select account
    Option = input("Please enter your UserID ")
    userInputStart(Option)

    # user input for chose of accounts
    UserChoose = input()
    userAccountChoice(UserChoose, Option)

    # Edit the account - add, minus or see balance
    userEditAccount(UserChoose, Option)

    # Restart program
    mainProgram()

# Call
mainProgram()
