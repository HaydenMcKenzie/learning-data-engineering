from ATM_Exam.src.main.filehandler.PrintName import gettingName


def askingOption(userID):
    print("Welcome " + gettingName(userID) + ". Please Enter an Option")
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


