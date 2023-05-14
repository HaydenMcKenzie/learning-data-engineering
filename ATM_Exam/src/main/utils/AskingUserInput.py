import sys

def startProgram():
    userIDInput = input("Please enter your UserID ")
    if "q" in userIDInput:
        sys.exit(1)
    return userIDInput