from cliConsole.utils import utils_print, utils_input, utils_db

userInfo = {}


def init():
    while True:
        userInfo['scope'] = utils_input.get_scope()
        userInfo['uid'] = utils_input.get_uid()
        userInfo['password'] = utils_input.get_password()
        userInfo['gender'] = utils_input.get_gender()
        userInfo['phoneNumber'] = utils_input.get_phone_number()

        if userInfo['scope'] == 'admin':
            pass
        elif userInfo['scope'] == 'guard':
            pass
        elif userInfo['scope'] == 'director':
            pass
        elif userInfo['scope'] == 'student':
            pass
        elif userInfo['scope'] == 'hod':
            pass
        elif userInfo['scope'] == 'warden':
            pass
        else:
            print("Invalid scope, config file out of sync")
            continue

        db_response = utils_db.add_user(userInfo)
        utils_print.pprint(db_response)
