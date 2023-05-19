from ATM_Exam.src.main.messages import AskingOption


'''import AskingUserInput as userIDInput
import EditOpeningAccountsData as OpeningAccData'''

"""def askingForFirstOption():s
    askingOption.answerOption()
    print("Which account do you wish to " + askingOption.passingAnswerOption() + " from:") # Reads user Option from askingOption()
    if userIDInput in OpeningAccData(): 
        accountTypeIndex = OpeningAccData().index(userIDInput) # Searches [userIDInput] in index
        peopleAcc = OpeningAccData.bankingInfo("ATM_Exam/data/OpeningAccountsData.txt")[accountTypeIndex] # Read row userIDInput in horizonally and into an array
        print("1 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")") # Prints AccountNumber and AccountType from OpeningAccountsData.txt

def askingForSecondOption():
    if userIDInput in OpeningAccData():
        accountTypeIndex2 = OpeningAccData().index(userIDInput) + 1 # Finds the first reference [userIDInput], finds the array number the +1 to it
        if accountTypeIndex2 < 6: # Array length is only 5. This stops the code from breaking
            peopleAcc = accountFile[accountTypeIndex2] # Read row userIDInput in horizonally and into an array
            print("2 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")") # Prints AccountNumber and AccountType from OpeningAccountsData.txt"""

AskingOption.askingOption()