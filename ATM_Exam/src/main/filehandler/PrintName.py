from ATM_Exam.src.main.filehandler.editfiles import removeDelimiter
from ATM_Exam.src.main.filehandler.editfiles import idsColumnUserInfo


def gettingName(userID):
    try:
        account = removeDelimiter("UserInfo.txt", ",")
        idIndex = idsColumnUserInfo().index(userID)
        accountIndex = account[idIndex]
        name = accountIndex[0:2]
        joinedName = " ".join(name)
        return joinedName
    except:
        pass


'''
answer = input("Enter ")
print(gettingName(answer))



def test():
    print("Welcome ", gettingName(answer), ". Please Enter an Option")
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')
'''
