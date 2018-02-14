from console.utils import utils_input, utils_db


def init():
    while True:
        print("[0] Return to previous menu")
        print("[1] Change Password")
        print("[2] Change Name")
        print("[3] Change Branch")
        choice = eval(input(">> "))
        if choice is 0:
            return
        elif choice is 1:
            change_password()
        elif choice is 2:
            change_name()
        elif choice is 3:
            change_branch()
        else:
            print("Invalid choice, try again")


def change_password():
    uid = utils_input.get_uid()
    user = utils_db.find_by_uid(uid)
    if user is not None:
        password = utils_input.generate_random_password()
        utils_db.update(uid, "password", password['hash'])
        print("New password: {}".format(password['password']))
        return
    else:
        print("User not found, please check the User ID")
        return


def change_name():
    uid = utils_input.get_uid()
    user = utils_db.find_by_uid(uid)
    if user is not None:
        print("Enter the name")
        name = utils_input.get_name()
        utils_db.update(uid, "name", name)
        print("Name changed from '{}' to '{}'".format(user['name'], name))
        return
    else:
        print("User not found, please check the User ID")
        return


def change_branch():
    uid = utils_input.get_uid()
    user = utils_db.find_by_uid(uid)
    if user is not None:
        branch = utils_input.get_branch()
        utils_db.update(uid, "branch", branch)
        print("Branch changed from '{}' to '{}'".format(user['branch'], branch))
