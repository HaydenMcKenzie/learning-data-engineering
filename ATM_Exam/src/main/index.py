import csv

def globalOption():
    global Option # { global variable }
    Option = input()

def dollarAdd(x, y):
    return "$" + f'{x + y:.2f}'

def dollarMinus(x, y):
    return "$" + f'{x - y:.2f}'

def personName():
    global name # { global variable }
    name = search_userID("ATM_Exam/main/UserInfo.txt", userIDInput) 

def bankingInfo(file_path):
    global accountFile 
    with open(file_path, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace("|||", "|") for line in file), delimiter='|')] # Reads file_path, changes "|||" to "|". Removes "|"
        accountType = [row[0] for row in accountFile]
        return accountType

def startProgram():
    global userIDInput # { global variable }
    userIDInput = input("Please enter your UserID ")
    if userIDInput == "q": 
        quit() 

def search_userID(userIDInput):
    with open(openUserInfoData(), 'r') as file:
        content = [item for item in csv.reader(file)]  # Removes ',' and forms and array
        ids = [row[3] for row in content] # Reads file vertically      
        while True: 
            try:
                idIndex = ids.index(userIDInput) # Reads input to match ID                
                people = content[idIndex] # Returns horizontal row 
                return people[0:2] # Returns first name and last name
            except ValueError:
                MainProgram() # Restart

def userAccountOption():
    name = search_userID(userIDInput) # FirstName and Surname from search_userID
    return " ".join(name) # Join FirstName and Surname

def askingOption():
    print("Welcome " + userAccountOption() + ". Please Enter an Option") # Calls the name from search_userID(file_path, userIDInput)
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')

def answerOption():
    askingOption()
    Option = input()
    if Option == "1":
        replaceOption = Option.replace("1", "Deposit")
    elif Option == "2":
        replaceOption = Option.replace("2", "Withdraw")
    elif Option == "3":
        replaceOption = Option.replace("3", "Balance")
    elif Option == "q":
        quit() 
    else:
        MainProgram()                                                          
    return replaceOption

def openOpeningAccData():
    return bankingInfo("ATM_Exam/data/OpeningAccountsData.txt")

def openUserInfoData():
    return "ATM_Exam/data/UserInfo.txt"

def askingChequeOrSavings(answerOptionPass):
    print("Which account do you wish to " + answerOptionPass + " from:") # Reads user Option from askingOption()
    if userIDInput in openOpeningAccData(): 
        accountTypeIndex = openOpeningAccData().index(userIDInput) # Searches [userIDInput] in index
        peopleAcc = accountFile[accountTypeIndex] # Read row userIDInput in horizonally and into an array
        print("1 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")") # Prints AccountNumber and AccountType from OpeningAccountsData.txt
        
    if userIDInput in openOpeningAccData():
        accountTypeIndex2 = openOpeningAccData().index(userIDInput) + 1 # Finds the first reference [userIDInput], finds the array number the +1 to it
        if accountTypeIndex2 < 6: # Array length is only 5. This stops the code from breaking
            peopleAcc = accountFile[accountTypeIndex2] # Read row userIDInput in horizonally and into an array
            print("2 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")") # Prints AccountNumber and AccountType from OpeningAccountsData.txt

def chequeAndSavings(answerOptionPass):
    global ChandSav
    ChandSav = input()

    if answerOptionPass == "Balance":     
        if ChandSav == '1':
            if userIDInput in openOpeningAccData():
                accountTypeIndex = openOpeningAccData().index(userIDInput)
                peopleAcc = accountFile[accountTypeIndex]  # Changes to a int
                print(peopleAcc[3])
                MainProgram()
                pass
                
        elif ChandSav == '2':
            if userIDInput in openOpeningAccData():
                accountTypeIndex2 = openOpeningAccData().index(userIDInput) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = accountFile[accountTypeIndex2]
                    print(peopleAcc[3])
                    MainProgram()
                    pass
        else:
            MainProgram()

    if ChandSav == '1':
        if userIDInput in openOpeningAccData():
            accountTypeIndex = openOpeningAccData().index(userIDInput)
            peopleAcc = accountFile[accountTypeIndex]
            print("How much do you wish to " + answerOptionPass + "? Balance = " + peopleAcc[3])
            pass
    elif ChandSav == '2':
        if userIDInput in openOpeningAccData():
            accountTypeIndex2 = openOpeningAccData().index(userIDInput) + 1
            if accountTypeIndex2 < 6:
                peopleAcc = accountFile[accountTypeIndex2]
                print("How much do you wish to " + answerOptionPass + "? Balance = " + peopleAcc[3])
                pass
    elif ChandSav == "q":
        quit()
    else:
        MainProgram()

def changing_C_Or_S_Account(answerOptionPass):
    userInput = int(input())

    if answerOptionPass == 'Deposit':  # Deposits
        if ChandSav == '1':  # First Option in OpeningAccountsData.txt
            if userIDInput in openOpeningAccData():
                accountTypeIndex = openOpeningAccData().index(userIDInput)
                peopleAcc = accountFile[accountTypeIndex]
                y = peopleAcc[3]
                z = [float(y)]
                print(dollarAdd(z[0], userInput))
        elif ChandSav == '2':  # Second Option in OpeningAccountsData.txt
            if userIDInput in openOpeningAccData():
                accountTypeIndex2 = openOpeningAccData().index(userIDInput) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = accountFile[accountTypeIndex2]
                    y = peopleAcc[3]
                    z = [float(y)]
                    print(dollarAdd(z[0], userInput))
        elif ChandSav == "q":
            quit()

    elif answerOptionPass == "Withdraw": # Withdraw                                  
        if ChandSav == "1": #First Option in OpeningAccountsData.txt
            if userIDInput in openOpeningAccData():
                accountTypeIndex = openOpeningAccData().index(userIDInput)
                peopleAcc = accountFile[accountTypeIndex]
                y = peopleAcc[3]
                z = [float(y)]
                if z[0] - userInput < 0:
                    print("Error")
                    MainProgram()
                else:
                    print(dollarMinus(z[0], userInput))

        elif ChandSav == "2": #Second Option in OpeningAccountsData.txt
            if userIDInput in openOpeningAccData():
                accountTypeIndex2 = openOpeningAccData().index(userIDInput) + 1 # Moves one more over in 
                if accountTypeIndex2 < 6:
                    peopleAcc = accountFile[accountTypeIndex2]
                    y = peopleAcc[3]
                    z = [float(y)]
                    if z[0] - userInput < 0:
                        print("Error")
                        MainProgram()
                    else:
                        print(dollarMinus(z[0], userInput))
        elif ChandSav == "q":
            quit()

def MainProgram():
    startProgram()
    search_userID(userIDInput)
    userAccountOption()
    answerOptionPass = answerOption()
    askingChequeOrSavings(answerOptionPass)
    chequeAndSavings(answerOptionPass)
    changing_C_Or_S_Account(answerOptionPass)
    MainProgram()

MainProgram()