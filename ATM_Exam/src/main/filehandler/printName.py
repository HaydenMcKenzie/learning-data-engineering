from ATM_Exam.src.main.filehandler.editfiles import removeDelimiter
from ATM_Exam.src.main.filehandler.editfiles import idsColumnUserInfo


def gettingName(userID):
    account = removeDelimiter("./data/UserInfo.txt", ",")
    idIndex = idsColumnUserInfo().index(userID)
    accountIndex = account[idIndex]
    name = accountIndex[0:2]
    joinedName = " ".join(name)
    return joinedName

# If you run, it will return John Smith
# print(gettingName("001"))
# If you get AskingOption.py in messages.
# My Error:
'''
Traceback (most recent call last):
  File "C:\Users\Hayden\PycharmProjects\DataAcademyATMExam\ATM_Exam\src\main\messages\AskingOption.py", line 1, in <module>
    from ATM_Exam.src.main.filehandler.printName import gettingName
  File "C:\Users\Hayden\PycharmProjects\DataAcademyATMExam\ATM_Exam\src\main\filehandler\printName.py", line 14, in <module>
    print(gettingName("001"))
  File "C:\Users\Hayden\PycharmProjects\DataAcademyATMExam\ATM_Exam\src\main\filehandler\printName.py", line 6, in gettingName
    account = removeDelimiter("./data/UserInfo.txt", ",")
  File "C:\Users\Hayden\PycharmProjects\DataAcademyATMExam\ATM_Exam\src\main\filehandler\editfiles.py", line 18, in removeDelimiter
    with open(filepath, 'r') as file:
FileNotFoundError: [Errno 2] No such file or directory: './data/UserInfo.txt'
'''

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