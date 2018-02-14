import bcrypt
import csv
import os

from console.utils import utils_print, utils_input, utils_db

fieldnames = [
    'uid',
    'email',
    'password',
    'name',
    'gender',
    'phoneNumber',
    'branch',
    'year',
    'roomNumber',
    'scope'

]

userInfo = {}


def init():
    while True:
        print("[0] Back To Previous Menu")
        print("[1] Enter Data For New User")
        print("[2] Create From data.csv File")
        query_type = input(">> ")
        if query_type is '0':
            return
        elif query_type is '1':
            create_new_user()
        elif query_type is '2':
            create_user_from_file()
        else:
            print("Invalid choice, try again")


def create_new_user():
    while True:
        password = utils_input.generate_random_password()
        user = {
            fieldnames[0]: utils_input.get_uid(),
            fieldnames[1]: utils_input.get_email(),
            fieldnames[2]: password['hash'],
            fieldnames[3]: utils_input.get_name(),
            fieldnames[4]: utils_input.get_gender(),
            fieldnames[5]: utils_input.get_phone_number(),
            fieldnames[9]: utils_input.get_scope()
        }

        if user['scope'] == 'admin':
            pass
        elif user['scope'] == 'guard':
            pass
        elif user['scope'] == 'director':
            pass
        elif user['scope'] == 'student':
            user[fieldnames[6]] = utils_input.get_branch()
            user[fieldnames[7]] = utils_input.get_year()
            user[fieldnames[8]] = utils_input.get_room_number()
        elif user['scope'] == 'hod':
            pass
        elif user['scope'] == 'warden':
            pass
        else:
            print("Invalid scope")
            continue

        utils_print.pprint(user)

        try:
            utils_db.add_user(user)
            print("User created with password: {}".format(password['password']))
            return
        except():
            print("Failed to create ->")
            utils_print.pprint(user)
            return


def create_user_from_file():
    path = os.path.join(os.getcwd(), 'console/data.csv')
    with open(path, newline='') as userFile:
        user_reader = csv.reader(userFile, delimiter=',', quotechar='|')
        for row in user_reader:
            user = {
                fieldnames[0]: row[0],
                fieldnames[1]: row[1],
                fieldnames[2]: str(bcrypt.hashpw(row[2].encode('utf-8'), bcrypt.gensalt(10)), 'utf-8'),
                fieldnames[3]: row[3],
                fieldnames[4]: row[4],
                fieldnames[5]: row[5],
                fieldnames[6]: row[6],
                fieldnames[7]: row[7],
                fieldnames[8]: row[8],
                fieldnames[9]: row[9]
            }
            utils_print.pprint(user)

            try:
                utils_db.add_user(user)
            except():
                print("Failed to create ->")
                utils_print.pprint(user)
