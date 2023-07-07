from ATM_Exam.src.main.accounts.AccountUsers import getAccount

def createForOpeningAccountsData(id, accountNo, accountType, value):
    """
    :return: Returns a custom-made account for OpeningAccountData.txt
    """
    account = id + "|||" + accountNo + "|||" + accountType + "|||" + value
    return account


def createForUserInfo(fname, lname, number, id):
    """
    :return: Returns a custom-made account for UserInfo.txt
    """
    account = fname + "," + lname + "," + number + "," + id
    return account


def pushToFiles():
    """
    :return: Adds 004|||5739824|||Saving|||500.00 to OpeningAccountsData.txt
    :return: Adds 004|||9771864|||Cheque|||42.00 to OpeningAccountsData.txt
    :return: Adds Hayden,McKenzie,0422530222,004 to UserInfo.txt
    """
    with open("../../../data/OpeningAccountsData.txt", 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(getAccount("003")[5], getAccount("003")[5] + "\n")

    with open("../../../data/OpeningAccountsData.txt", "w") as file:
        account1 = createForOpeningAccountsData("004", "5739824", "Saving", "500.00\n")
        account2 = createForOpeningAccountsData("004", "9771864", "Cheque", "42.00")
        file.write(filedata)
        file.write(account1)
        file.write(account2)

    with open("../../../data/UserInfo.txt", 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(getAccount("003")[2], getAccount("003")[2] + "\n")

    with open("../../../data/UserInfo.txt", "w") as file:
        account = createForUserInfo("Hayden", "McKenzie", "0422530222", "004")
        file.write(filedata)
        file.write(account)


def deleteInfo():
    """
    :return: Resets OpeningAccountsData.txt
    :return: Resets UserInfo.txt
    """
    with open("../../../data/OpeningAccountsData.txt", 'r+') as file:
        filedata = file.read()

    info = '''AccountOwnerID|||AccountNumber|||AccountType|||OpeningBalance
001|||9264945|||Cheque|||500.09
001|||7814135|||Saving|||200.09
002|||9676422|||Saving|||1200.00
002|||7524155|||Cheque|||50.00
003|||9042221|||Saving|||4000.20'''

    with open("../../../data/OpeningAccountsData.txt", "w") as file:
        file.write(info)

    with open("../../../data/UserInfo.txt", 'r') as file:
        filedata = file.read()

    info = '''FirstName,Surname,Mobile,AccountOwnerID
John,Smith,0403715629,001
Leanne,Smith,0403185031,002
Kim,Kash,0404993021,003'''

    with open("../../../data/UserInfo.txt", "w") as file:
        file.write(info)


#pushToFiles()
deleteInfo()