from ATM_Exam.src.main.filehandler.readUserInfo import listAccountsID


class Account:
    def __init__(self, fname, lname, userId):
        self.fname = fname
        self.lname = lname
        self.userId = userId

