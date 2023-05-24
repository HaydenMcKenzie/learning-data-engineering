from ATM_Exam.src.main.filehandler.editfiles import removeDelimiter
from ATM_Exam.src.main.filehandler.editfiles import firstColumn


def gettingName(userID):
    account = removeDelimiter("./data/UserInfo.txt", ",")
    idIndex = firstColumn().index(userID)
    accountIndex = account[idIndex]
    name = accountIndex[0:2]
    joinedName = " ".join(name)
    return joinedName

answer = input("Enter ")
print(gettingName(answer))

def test():
    print("Welcome ", gettingName(answer), ". Please Enter an Option")
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')

test()