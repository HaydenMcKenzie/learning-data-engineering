


def mainProgram():
    bankAccount = 1000

    enterUserID = input("Enter a user ID: ")
    while enterUserID != 'q':
        print("Welcome to the ATM")
        print("Please choose an option:")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Balance")
        print("q. quit")
        if enterUserID == "q":
            print("Thank you")
            quit()
        break
    else:
        print("Thank you")
        quit()

    enterOption = input("Enter Option: ")

    if enterOption == "1":
        amount = int(input("How much do you want to Deposit"))
        newBalance = bankAccount + amount
        print("your new balance is:", newBalance)
        mainProgram()
    elif enterOption == "2":
        amount = int(input("How much do you want to Withdrawal"))
        newBalance = bankAccount - amount
        print("your new balance is:", newBalance)
        mainProgram()
    elif enterOption == "3":
        print("Your balance is: ", bankAccount)
        mainProgram()
    elif enterOption == "q":
        print("Thank you")
        quit()
    else:
        print("Try again")
        mainProgram()


mainProgram()

