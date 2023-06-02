from ATM_Exam.src.main.filehandler.readUserInfo import listAccountsID
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccounts
from ATM_Exam.src.main.filehandler.readOpeningAccountData import listAccountsForSecondAccount

'''
Same code as ATM_Exam.src.main.messages.AskingOption import GettingChOrSav
Difference it gets the first account details 
'''

def getAccount(accountID):
    return listAccountsID(accountID)[0], listAccountsID(accountID)[1], listAccounts(accountID)[0], \
           listAccounts(accountID)[1], listAccounts(accountID)[2], listAccounts(accountID)[3]


'''
Same code as ATM_Exam.src.main.messages.AskingOption import GettingChOrSav
Difference it gets the second account details if there is an account account
'''
def getSecondAccount(accountID):
    ifAccountIsThere = listAccountsForSecondAccount(accountID)
    if ifAccountIsThere:
        return listAccountsID(accountID)[0], listAccountsID(accountID)[1], listAccountsForSecondAccount(accountID)[0], listAccountsForSecondAccount(accountID)[1], listAccountsForSecondAccount(accountID)[2], listAccountsForSecondAccount(accountID)[3]

