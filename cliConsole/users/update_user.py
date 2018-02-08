from cliConsole.users.update import password


def init():
    while True:
        print("[0] Return to previous menu")
        print("[1] Update Password")
        choice = eval(input(">> "))
        if choice is 0:
            return
        if choice is 1:
            password.init()
