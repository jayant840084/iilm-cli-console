from . import create_user, update_user, find_user, remove_user


def init():
    while True:
        print("[0] Return to previous menu")
        print("[1] Create user")
        print("[2] Update user")
        print("[3] Find user")
        # print("[4] Remove user")
        choice = eval(input(">> "))
        if choice is 0:
            return
        if choice is 1:
            create_user.init()
        elif choice is 2:
            update_user.init()
        elif choice is 3:
            find_user.init()
        elif choice is 4:
            remove_user.init()
