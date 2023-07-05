from ATM_Exam.src.main.filehandler.PrintName import gettingName
from ATM_Exam.src.main.messages.QuitingMessage import printingBalancesOfAccounts

def askingOption(userID):
    """
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: receives the first name and last name from gettingname() and adds it to the message
    """
    print("Welcome " + gettingName(userID) + ". Please Enter an Option")
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')

def answerOption(option):
    """
    :param option: User Input from ATM.py - Either 1, 2, 3 or q
    :return: Takes Option and replaced with corresponding word and adds it to message and/or quits
    """
    if option == "1":
        replaceOption = option.replace("1", "Deposit")
        return "Which account do you wish to " + replaceOption + " to:"
    elif option == "2":
        replaceOption = option.replace("2", "Withdraw")
        return "Which account do you wish to " + replaceOption + " from:"
    elif option == "3":
        replaceOption = option.replace("3", "Balance")
        return "Which account do you wish to see the " + replaceOption + " of:"
    elif option == "q":
        printingBalancesOfAccounts()
        quit()

