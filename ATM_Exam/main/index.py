import csv

def StartProgram():
    global userIDInput # { global variable }
    userIDInput = input("Enter a Number: ")
    if userIDInput == "q": 
        quit() 

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
    global accountType # { global variable }
    global filez # { global variable }
    with open(file_path, 'r') as file:
        filez = [item for item in csv.reader((line.replace("|||", "|") for line in file), delimiter='|')] # Reads file_path, changes "|||" to "|". Removes "|"
        accountType = [row[0] for row in filez]


def search_userID(file_path, userIDInput):
    with open(file_path, 'r') as file:
        content = [item for item in csv.reader(file)]  # Removes ',' and forms and array
        ids = [row[3] for row in content]              # Reads file vertically      
        while True: 
            try:
                idIndex = ids.index(userIDInput)              # Reads input to match ID                
                people = content[idIndex]              # Returns horizontal row 
                return people[0:2]                     # Returns first name and last name
            except ValueError:
                userIDInput = input("Enter a Number: ")
                     
def userAccountOption():
    name = search_userID("ATM_Exam/main/UserInfo.txt", userIDInput) 
    return " ".join(name)

def askingChequeOrSavings():
    print("Which account do you wish to " + replaceOption + " from:")
    bankingInfo("ATM_Exam/main/OpeningAccountsData.txt") 
    if userIDInput in accountType:
        accountTypeIndex = accountType.index(userIDInput)
        peopleAcc = filez[accountTypeIndex]
        print("1 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")")
    if userIDInput in accountType:
        accountTypeIndex2 = accountType.index(userIDInput) + 1
        if accountTypeIndex2 < 6:
            peopleAcc = filez[accountTypeIndex2]
            print("2 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")")

def askingOption():
    global replaceOption # { global variable }
    print("Welcome " + userAccountOption() + ". Please Enter an Option") # Calls the name from search_userID(file_path, userIDInput)
    print('1 For Deposits')
    print('2 For Withdraw')
    print('3 For Balance')
    print('q To Quit')
    while True:
        globalOption() # Option = input()
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
            else: # Restart the Application
                MainProgram()                                                          
        except:
            quit()

def changing_C_Or_S_Account(file_path):
    bankingInfo("ATM_Exam/main/OpeningAccountsData.txt")
    userInput = int(input())

    if Option == '1':  # Deposits
        if ChandSav == '1':  # First Option in OpeningAccountsData.txt
            if userIDInput in accountType:
                accountTypeIndex = accountType.index(userIDInput)
                peopleAcc = filez[accountTypeIndex]
                y = peopleAcc[3]
                z = [float(y)]
                print(dollarAdd(z[0], userInput))
        elif ChandSav == '2':  # Second Option in OpeningAccountsData.txt
            if userIDInput in accountType:
                accountTypeIndex2 = accountType.index(userIDInput) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = filez[accountTypeIndex2]
                    y = peopleAcc[3]
                    z = [float(y)]
                    print(dollarAdd(z[0], userInput))
        elif ChandSav == "q":
            quit()

    if Option == "2": # Withdraw                                  
        if ChandSav == "1": #First Option in OpeningAccountsData.txt
            if userIDInput in accountType:
                accountTypeIndex = accountType.index(userIDInput)
                peopleAcc = filez[accountTypeIndex]
                y = peopleAcc[3]
                z = [float(y)]
                if z[0] - userInput < 0:
                    print("Error")
                    MainProgram()
                else:
                    print(dollarMinus(z[0], userInput))

        elif ChandSav == "2": #Second Option in OpeningAccountsData.txt
            if userIDInput in accountType:
                accountTypeIndex2 = accountType.index(userIDInput) + 1 # Moves one more over in 
                if accountTypeIndex2 < 6:
                    peopleAcc = filez[accountTypeIndex2]
                    y = peopleAcc[3]
                    z = [float(y)]
                    if z[0] - userInput < 0:
                        print("Error")
                        MainProgram()
                    else:
                        print(dollarMinus(z[0], userInput))
        elif ChandSav == "q":
            quit()

def chequeAndSavings(file_path):
    global ChandSav
    global replaceOption2
    bankingInfo("ATM_Exam/main/OpeningAccountsData.txt")
    test = userIDInput

    ChandSav = input()

    if Option == "1":
        replaceOption2 = Option.replace("1", "Deposit")
    elif Option == "2":
        replaceOption2 = Option.replace("2", "Withdraw")
    elif Option == "3":
        replaceOption2 = Option.replace("3", "Balance")
        
        if ChandSav == '1':
            if test in accountType:
                accountTypeIndex = accountType.index(userIDInput)
                peopleAcc = filez[accountTypeIndex]  
                print(peopleAcc[3])
                MainProgram()
                pass
                
        elif ChandSav == '2':
            if test in accountType:
                accountTypeIndex2 = accountType.index(userIDInput) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = filez[accountTypeIndex2]
                    print(peopleAcc[3])
                    MainProgram()
                    pass

        else:
            MainProgram()

    while True:
        try:
            if ChandSav == '1':
                if test in accountType:
                    accountTypeIndex = accountType.index(userIDInput)
                    peopleAcc = filez[accountTypeIndex]
                    print("How much do you wish to " + replaceOption2 + "? Balance = " + peopleAcc[3])
                    break
            elif ChandSav == '2':
                if test in accountType:
                    accountTypeIndex2 = accountType.index(userIDInput) + 1
                    if accountTypeIndex2 < 6:
                        peopleAcc = filez[accountTypeIndex2]
                        print("How much do you wish to " + replaceOption2 + "? Balance = " + peopleAcc[3])
                        break
            elif ChandSav == "q":
                    quit()
            else:
                MainProgram()
        except:
            MainProgram()
    
def MainProgram():
    while True:
        try:
            StartProgram()
            search_userID("ATM_Exam/main/UserInfo.txt", userIDInput)
            userAccountOption()
            askingOption()
            askingChequeOrSavings()
            chequeAndSavings("ATM_Exam/main/OpeningAccountsData.txt")
            changing_C_Or_S_Account("ATM_Exam/main/OpeningAccountsData.txt")
        except:
            quit()

MainProgram()