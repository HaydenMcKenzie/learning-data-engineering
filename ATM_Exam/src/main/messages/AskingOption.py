from ATM_Exam.src.main.filehandler.printName import gettingName

from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount

def askingOption(userID):
    print("Welcome " + gettingName(userID) + ". Please Enter an Option") # Calls the name from search_userID(file_path, userIDInput)
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')


def answerOption(Option):
    if Option == "1":
        replaceOption = Option.replace("1", "Deposit")
        print("Which account do you wish to " + replaceOption + " to:")
    elif Option == "2":
        replaceOption = Option.replace("2", "Withdraw")
        print("Which account do you wish to " + replaceOption + " from:")
    elif Option == "3":
        replaceOption = Option.replace("3", "Balance")
        print("Which account do you wish to see the " + replaceOption + " of:")
    elif Option == "q":
        quit()

def testingGettingChOrSav(UserID):
    print("1 for", listAccounts(UserID)[1], "(" + listAccounts(UserID)[2] + ")")
    ifAccountIsThere = listAccountsForSecondAccount(UserID)
    if ifAccountIsThere:
        print("2 for", listAccountsForSecondAccount(UserID)[1], "(" + listAccountsForSecondAccount(UserID)[2] + ")")

'''
from ATM_Exam.src.main.filehandler.printName import gettingName

userID = "001"
name = gettingName(userID)
print(name)



def test():
    print("Welcome ", gettingName(answer), ". Please Enter an Option")
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')

test()


def answerOption():
    askingOption()
    Option = input()
    return Option

def passingAnswerOption():
    if answerOption() == "1":
        replaceOption = answerOption().replace("1", "Deposit")
        return replaceOption
    elif answerOption() == "2":
        replaceOption = answerOption().replace("2", "Withdraw")
        return replaceOption
    elif answerOption() == "3":
        replaceOption = answerOption().replace("3", "Balance")
        return replaceOption
    elif answerOption() == "q":
        quit() 
    else:  
'''