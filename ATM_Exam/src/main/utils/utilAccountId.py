from ATM_Exam.src.main.messages.AskingOption import askingOption

def userAccountID(Option):
    try:
        if Option != "q":
            askingOption(Option)
        else:
            try:
                quit()
            except TypeError:
                quit()
    except TypeError:
        userAccountID(Option)