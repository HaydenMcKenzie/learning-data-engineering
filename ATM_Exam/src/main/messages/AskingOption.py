import ATM_Exam.src.main.accounts.OpenUserInfo as UserInfoFile

"""class testingOption():
    @staticmethod
    def __init__():
        pass"""

def askingOption():
    print("Welcome " + UserInfoFile.userAccountOption() + ". Please Enter an Option") # Calls the name from search_userID(file_path, userIDInput)
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')

def answerOption():
    askingOption()
    Option = input()
    return Option

def passingAnswerOption():
    if answerOption() == "1":
        replaceOption = answerOption().replace("1", "Deposit")
    elif answerOption() == "2":
        replaceOption = answerOption().replace("2", "Withdraw")
    elif answerOption() == "3":
        replaceOption = answerOption().replace("3", "Balance")
    elif answerOption() == "q":
        quit() 
    else:
        quit()                                                        
    return replaceOption        