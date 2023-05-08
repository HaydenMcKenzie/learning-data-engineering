import csv


def startProgram():
    global userIDInput
    userIDInput = input("Please enter your User ID: ")


def globalOption():
    global Option
    Option = input()


def dollarAdd(x, y):
    return "$" + f'{x + y:.2f}'


def dollarMinus(x, y):
    return "$" + f'{x - y:.2f}'


def bankingInfo(file_path):
    global accountType
    global accountFile
    with open(file_path, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace("|||", "|") for line in file), delimiter='|')]
        accountType = [row[0] for row in accountFile]

startProgram()

def search_userID(file_path, userIDInput):
    with open(file_path, 'r') as file:
        content = [item for item in csv.reader(file)] #Reads files. Removes ','. Makes in array
        ids = [row[3] for row in content] #Reads verically
        while True:
            try:
                idIndex = ids.index(userIDInput) #001 002 003
                people = content[idIndex] #Reads horizonally
                return people[0:2] #Fname and lname
            except ValueError:
                userIDInput = input("Enter a Number: ")


name = search_userID("ATM_Exam/main/UserInfo.txt", userIDInput) #"project_ATMExam/root/UserInfo.txt"

def userAccountOption():
    return " ".join(name)

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
                startProgram()
                search_userID("ATM_Exam/main/UserInfo.txt", userIDInput)
                userAccountOption()
                askingOption()
                pass
        except:
            quit()

def askingChequeOrSavings():
    print("Which account do you wish to " + replaceOption + " from:")
    bankingInfo("ATM_Exam/main/OpeningAccountsData.txt") #"project_ATMExam/root/OpeningAccountsData.txt"
    if userIDInput in accountType:
        accountTypeIndex = accountType.index(userIDInput)
        peopleAcc = accountFile[accountTypeIndex]
        print("1 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")")
    if userIDInput in accountType:
        accountTypeIndex2 = accountType.index(userIDInput) + 1
        if accountTypeIndex2 < 6:
            peopleAcc = accountFile[accountTypeIndex2]
            print("2 for " + peopleAcc[1] + " " + "(" + peopleAcc[2] + ")")

askingOption()
askingChequeOrSavings()

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
                peopleAcc = accountFile[accountTypeIndex]  # Changes to a int
                print(peopleAcc[3])
                quit()
        if ChandSav == '2':
            if test in accountType:
                accountTypeIndex2 = accountType.index(userIDInput) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = accountFile[accountTypeIndex2]
                    print(peopleAcc[3])
                    quit()

    while True:
        try:
            if ChandSav == '1':
                if test in accountType:
                    accountTypeIndex = accountType.index(userIDInput)
                    peopleAcc = accountFile[accountTypeIndex]
                    print("How much do you wish to " + replaceOption2 + "? Balance = " + peopleAcc[3])
                    break
            elif ChandSav == '2':
                if test in accountType:
                    accountTypeIndex2 = accountType.index(userIDInput) + 1
                    if accountTypeIndex2 < 6:
                        peopleAcc = accountFile[accountTypeIndex2]
                        print("How much do you wish to " + replaceOption2 + "? Balance = " + peopleAcc[3])
                        break
            else:
                startProgram()
                search_userID("ATM_Exam/main/UserInfo.txt", userIDInput)
                userAccountOption()
                askingOption()
                askingChequeOrSavings()
                chequeAndSavings("ATM_Exam/main/OpeningAccountsData.txt")
                break
        except:
            quit()

def changing_C_Or_S_Account(file_path):
    # print("ChandSav = " + ChandSav)
    # print("Option equals = " + Option)
    bankingInfo("ATM_Exam/main/OpeningAccountsData.txt")
    userInput = int(input())

    if Option == '1':  # Deposits
        if ChandSav == '1':  # First Option in Bank.txt
            if userIDInput in accountType:
                accountTypeIndex = accountType.index(userIDInput)
                peopleAcc = accountFile[accountTypeIndex]
                y = peopleAcc[3]
                z = [float(y)]
                print(dollarAdd(z[0], userInput))
        elif ChandSav == '2':  # Second Option in Bank.txt
            if userIDInput in accountType:
                accountTypeIndex2 = accountType.index(userIDInput) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = accountFile[accountTypeIndex2]
                    y = peopleAcc[3]
                    z = [float(y)]
                    print(dollarAdd(z[0], userInput))

    if Option == "2":
        if ChandSav == "1":
            if userIDInput in accountType:
                accountTypeIndex = accountType.index(userIDInput)
                peopleAcc = accountFile[accountTypeIndex]
                y = peopleAcc[3]
                z = [float(y)]
                if z[0] - userInput < 0:
                    print("Error")
                    startProgram()
                    search_userID("ATM_Exam/main/UserInfo.txt", userIDInput)
                    userAccountOption()
                    askingOption()
                    askingChequeOrSavings()
                    chequeAndSavings("ATM_Exam/main/OpeningAccountsData.txt")
                    changing_C_Or_S_Account("ATM_Exam/main/OpeningAccountsData.txt")
                else:
                    print(dollarMinus(z[0], userInput))

        elif ChandSav == "2":
            if userIDInput in accountType:
                accountTypeIndex2 = accountType.index(userIDInput) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = accountFile[accountTypeIndex2]
                    y = peopleAcc[3]
                    z = [float(y)]
                    if z[0] - userInput < 0:
                        print("Error")
                        startProgram()
                        search_userID("ATM_Exam/main/UserInfo.txt", userIDInput)
                        userAccountOption()
                        askingOption()
                        askingChequeOrSavings()
                        chequeAndSavings("ATM_Exam/main/OpeningAccountsData.txt")
                        changing_C_Or_S_Account("ATM_Exam/main/OpeningAccountsData.txt")
                    else:
                        print(dollarMinus(z[0], userInput))

chequeAndSavings("ATM_Exam/main/OpeningAccountsData.txt")
changing_C_Or_S_Account("ATM_Exam/main/OpeningAccountsData.txt")

def startOverAgain():
    print("End")

startOverAgain()

'''                   
        if Option == "2":
            if "003" in accountType:
                accountTypeIndex = accountType.index(test)
                peopleAcc = accountFile[accountTypeIndex]
                y = peopleAcc[3]  # Selects all numerical numbers
                z = [float(y)]  # Changes to a int
                print(z[0] - userInput)
            if test in accountType:
                accountTypeIndex2 = accountType.index(test) + 1
                if accountTypeIndex2 < 6:
                    peopleAcc = accountFile[accountTypeIndex2]
                    y = peopleAcc[3]  # Selects all numerical numbers
                    z = [float(y)]  # Changes to a int
                    print(z[0] - userInput)
'''