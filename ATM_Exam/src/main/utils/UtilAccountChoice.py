from ATM_Exam.src.main.messages.AskingOption import answerOption
from ATM_Exam.src.main.accounts.AccountUsers import printAccountOptions
from ATM_Exam.src.main.messages.QuitingMessage import printingBalancesOfAccounts

def userAccountChoice(input, userID):
    """
    :param input: User Input from ATM.py - Either 1, 2, 3 or q
    :param userID: User Input from ATM.py - Either 001, 002 or 003
    :return: Returns command (e.g. Deposit) and shows accounts associated with userID
    """
    try:
        if input == "1":
            print(answerOption(input))
            printAccountOptions(userID)
        elif input == "2":
            print(answerOption(input))
            printAccountOptions(userID)
        elif input == "3":
            print(answerOption(input))
            printAccountOptions(userID)
        elif input == "q":
            printingBalancesOfAccounts()
            quit()
        else:
            print("Error - Wrong Input: Please enter valid option")
    except TypeError:
        print("Error - Wrong Input: Please enter valid option")
        userAccountChoice(input, userID)
    except ValueError:
        print("Error - Wrong Input: Please enter valid option")
        userAccountChoice(input, userID)
