from console.users import users
from console.utils import utils_input


if __name__ == '__main__':
    while True:
        print("Select a sub module")
        print("[1] Users")
        print("[0] Exit")
        choice = input(">> ")

        if choice is '0':
            exit(0)
        elif choice is '1':
            users.init()
        elif choice is '2':
            pass
        elif choice is '3':
            pass
        else:
            print("Invalid input")
