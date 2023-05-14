import csv
import ATM_Exam.src.main.utils.AskingUserInput as userIDInput

def openUserInfoData():
    return "ATM_Exam/data/UserInfo.txt"

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
                quit()

def userAccountOption():
    name = search_userID(userIDInput) # FirstName and Surname from search_userID
    return " ".join(name) # Join FirstName and Surname