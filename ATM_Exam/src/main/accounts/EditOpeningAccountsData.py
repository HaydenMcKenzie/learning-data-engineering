import csv


def bankingInfo(file_path):
    with open(file_path, 'r') as file:
        accountFile = [item for item in csv.reader((line.replace("|||", "|") for line in file), delimiter='|')]  # Reads file_path, changes "|||" to "|". Removes "|"
        return accountFile


#print("AccountFile", bankingInfo("ATM_Exam/src/main/data/OpeningAccountsData.txt"))
print("AccountFile", bankingInfo("../filehandler/data/OpeningAccountsData.txt"))


def ReturnBankingInfo():
    accountType = [row[0] for row in bankingInfo("../filehandler/data/OpeningAccountsData.txt")]
    return accountType


print("AccountType", ReturnBankingInfo())
