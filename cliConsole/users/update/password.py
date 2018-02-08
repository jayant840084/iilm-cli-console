from cliConsole.utils import utils_input, utils_db

import string
import random
import bcrypt


def init():
    while True:
        uid = utils_input.get_uid()
        user = utils_db.find_by_uid(uid)
        if user is not None:
            password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            password_hash = str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10)), 'utf-8')
            utils_db.update_password(uid, password_hash)
            print("New password: {}".format(password))
            return
        else:
            print("User not found, please check the User ID")
