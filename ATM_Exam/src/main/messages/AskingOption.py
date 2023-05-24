from ATM_Exam.src.main.filehandler.printName import gettingName

numberTest = "001"
name = gettingName(numberTest)
print(name)

'''
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
