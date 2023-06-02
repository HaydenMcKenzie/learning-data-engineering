from ATM_Exam.src.main.filehandler.editfiles import removeDelimiter
from ATM_Exam.src.main.filehandler.editfiles import idsColumnOpenAccountData
from ATM_Exam.src.main.filehandler.editfiles import idsColumnUserInfo



'''
Function listAccounts with variable of userID
account = removeDelimiter(filepath and removeDel)
idIndex = index userID in firstColumn()  
accountIndex = The first line with userID
return accountIndex 
'''
def listAccounts(userID):
    account = removeDelimiter("OpeningAccountsData.txt", "|||")
    idIndex = idsColumnOpenAccountData().index(userID)
    accountIndex = account[idIndex]
    return accountIndex

'''
Function listAccountsForSecondAccount with variable of userID
try to see if there is a second account
account = removeDelimiter(filepath and removeDel)
idIndex = index userID in firstColumn() then move one down 
accountIndex = The second line with userID
return accountIndex 
except IndexError, then pass
'''
def listAccountsForSecondAccount(userID):
    try:
        account = removeDelimiter("OpeningAccountsData.txt", "|||")
        idIndex = idsColumnOpenAccountData().index(userID) + 1
        accountIndex = account[idIndex]
        return accountIndex
    except IndexError:
        pass


# The code in the main file.
#answer = input("Enter ")
#print(listAccounts(answer))
#print("1 for", listAccounts(answer)[1], "(" + listAccounts(answer)[2] + ")")
#ifAccountIsThere = listAccountsForSecondAccount(answer)
#if ifAccountIsThere:
#    print("2 for", listAccountsForSecondAccount(answer)[1], "(" + listAccountsForSecondAccount(answer)[2] + ")")


'''
print(listAccounts("001"))
print(listAccounts("002"))
print(listAccounts("003"))
'''

'''
For Future 
        choose = accountFile[0]
        choose1 = choose[0:2]
        name = " ".join(choose1)
print FirstName Surname
'''
