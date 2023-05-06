'''
WRITE Please enter your User ID
INPUT userID
PRINT Welcome fname lname. Please Enter an Option
INPUT userOptionChoice
CASE option of 
    1: PRINT 1 for Deposits
    2: PRINT 2 for Withdraw
    3: PRINT 3 for Balance
    q: PRINT q to Quit
OTHERS 
    PRINT Please enter 1, 2, 3 or q
ENDCASE
PRINT Which account do you wish to Withdraw from:
Input userAccountChoice
CASE account of 
    1: PRINT 1 for chequeNo (Cheque)
    2: PRINT 2 for savingNo (Saving)
OTHERS 
    PRINT Please enter 1 or 2
ENDCASE
PRINT How much do you wihs to withdraw? Balance = chequeBal or savingBal
INPUT userWithdrawAmount
IF amount <= balance THEN
    Balance - userWithdrawAmount
    PRINT Withdrawal is successful. Your bank balance is now chequeBal or savingBal
ELSE:
    PRINT Error - Wrong Input. Amount Entered (userWithdrawAmount) is greater than amount in account (chequeBal or savingBal) 
ENDIF
'''

import csv


def StartProgram():
    global word
    word = input("Enter a Number: ")


def globalOption():
    global Option
    Option = input()


def dollarAdd(x, y):
    return "$" + f'{x + y:.2f}'


def dollarMinus(x, y):
    return "$" + f'{x - y:.2f}'


def bankingInfo(file_path):
    global accountType
    global filez
    with open(file_path, 'r') as file:
        filez = [item for item in csv.reader((line.replace("|||", "|") for line in file), delimiter='|')]
        accountType = [row[0] for row in filez]

StartProgram()

def search_userID(file_path, word):
    with open(file_path, 'r') as file:
        content = [item for item in csv.reader(file)] #Reads files. Removes ','. Makes in array
        ids = [row[3] for row in content] #Reads verically
        while True:
            try:
                idIndex = ids.index(word) #001 002 003
                people = content[idIndex] #Reads horizonally
                return people[0:2] #Fname and lname
            except ValueError:
                word = input("Enter a Number: ")


name = search_userID("project_ATMExam/main/UserInfo.txt", word) #"project_ATMExam/root/UserInfo.txt"

def userAccountOption():
    return " ".join(name)

def askingChequeOrSavings():
    print("Which account do you wish to " + replaceOption + " from:")
    bankingInfo("project_ATMExam/main/OpeningAccountsData.txt") #"project_ATMExam/root/OpeningAccountsData.txt"
    if word in accountType:
        accountTypeIndex = accountType.index(word)
        peopleAcc = filez[accountTypeIndex]
        print("1 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")")
    if word in accountType:
        accountTypeIndex2 = accountType.index(word) + 1
        if accountTypeIndex2 < 6:
            peopleAcc = filez[accountTypeIndex2]
            print("2 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")")

def askingOption():
    global replaceOption
    print("Welcome " + userAccountOption() + ". Please Enter an Option")
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')
    while True:
        globalOption()
        try:
            if Option == "1":
                replaceOption = Option.replace("1", "Deposit")
                break
            elif Option == "2":
                replaceOption = Option.replace("2", "Withdraw")
                break
            elif Option == "3":
                replaceOption = Option.replace("3", "Balance")
                break
            elif Option == "q":
                quit()
            else:
                StartProgram()
                search_userID("project_ATMExam/main/UserInfo.txt", word)
                userAccountOption()
                askingOption()
                pass
        except:
            quit()

askingOption()
askingChequeOrSavings()

def changing_C_Or_S_Account(file_path):
    # print("ChandSav = " + ChandSav)
    # print("Option equals = " + Option)
    bankingInfo("project_ATMExam/main/OpeningAccountsData.txt")
    userInput = int(input())
    test = Option

    if Option == '1':  # Deposits
        if ChandSav == '1':  # First Option in Bank.txt
            if word in accountType:
                accountTypeIndex = accountType.index(word)
                peopleAcc = filez[accountTypeIndex]
                y = peopleAcc[3]
                z = [float(y)]
                print(dollarAdd(z[0], userInput))
        elif ChandSav == '2':  # Second Option in Bank.txt
            if word in accountType:
                accountTypeIndex2 = accountType.index(word) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = filez[accountTypeIndex2]
                    y = peopleAcc[3]
                    z = [float(y)]
                    print(dollarAdd(z[0], userInput))

    if Option == "2":
        if ChandSav == "1":
            if word in accountType:
                accountTypeIndex = accountType.index(word)
                peopleAcc = filez[accountTypeIndex]
                y = peopleAcc[3]
                z = [float(y)]
                if z[0] - userInput < 0:
                    print("Error")
                    StartProgram()
                    search_userID("project_ATMExam/main/UserInfo.txt", word)
                    userAccountOption()
                    askingOption()
                    askingChequeOrSavings()
                    chequeAndSavings("project_ATMExam/main/OpeningAccountsData.txt")
                    changing_C_Or_S_Account("project_ATMExam/main/OpeningAccountsData.txt")
                else:
                    print(dollarMinus(z[0], userInput))

        elif ChandSav == "2":
            if word in accountType:
                accountTypeIndex2 = accountType.index(word) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = filez[accountTypeIndex2]
                    y = peopleAcc[3]
                    z = [float(y)]
                    if z[0] - userInput < 0:
                        print("Error")
                        StartProgram()
                        search_userID("project_ATMExam/main/UserInfo.txt", word)
                        userAccountOption()
                        askingOption()
                        askingChequeOrSavings()
                        chequeAndSavings("project_ATMExam/main/OpeningAccountsData.txt")
                        changing_C_Or_S_Account("project_ATMExam/main/OpeningAccountsData.txt")
                    else:
                        print(dollarMinus(z[0], userInput))

def chequeAndSavings(file_path):
    global ChandSav
    global replaceOption2
    bankingInfo("project_ATMExam/main/OpeningAccountsData.txt")
    test = word

    ChandSav = input()

    if Option == "1":
        replaceOption2 = Option.replace("1", "Deposit")
    elif Option == "2":
        replaceOption2 = Option.replace("2", "Withdraw")
    elif Option == "3":
        replaceOption2 = Option.replace("3", "Balance")
        if ChandSav == '1':
            if test in accountType:
                accountTypeIndex = accountType.index(word)
                peopleAcc = filez[accountTypeIndex]  # Changes to a int
                print(peopleAcc[3])
                quit()
        if ChandSav == '2':
            if test in accountType:
                accountTypeIndex2 = accountType.index(word) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = filez[accountTypeIndex2]
                    print(peopleAcc[3])
                    quit()

    while True:
        try:
            if ChandSav == '1':
                if test in accountType:
                    accountTypeIndex = accountType.index(word)
                    peopleAcc = filez[accountTypeIndex]
                    print("How much do you wish to " + replaceOption2 + "? Balance = " + peopleAcc[3])
                    break
            elif ChandSav == '2':
                if test in accountType:
                    accountTypeIndex2 = accountType.index(word) + 1
                    if accountTypeIndex2 < 6:
                        peopleAcc = filez[accountTypeIndex2]
                        print("How much do you wish to " + replaceOption2 + "? Balance = " + peopleAcc[3])
                        break
            else:
                StartProgram()
                search_userID("project_ATMExam/main/UserInfo.txt", word)
                userAccountOption()
                askingOption()
                askingChequeOrSavings()
                chequeAndSavings("project_ATMExam/main/OpeningAccountsData.txt")
                break
        except:
            quit()

chequeAndSavings("project_ATMExam/main/OpeningAccountsData.txt")
changing_C_Or_S_Account("project_ATMExam/main/OpeningAccountsData.txt")

def startOverAgain():
    print("End")

startOverAgain()
'''                   
        if Option == "2":
            if "003" in accountType:
                accountTypeIndex = accountType.index(test)
                peopleAcc = filez[accountTypeIndex]
                y = peopleAcc[3]  # Selects all numerical numbers
                z = [float(y)]  # Changes to a int
                print(z[0] - userInput)
            if test in accountType:
                accountTypeIndex2 = accountType.index(test) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = filez[accountTypeIndex2]
                    y = peopleAcc[3]  # Selects all numerical numbers
                    z = [float(y)]  # Changes to a int
                    print(z[0] - userInput)
'''