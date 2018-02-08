import bcrypt

from cliConsole import config


def get_scope():
    constraints = config.user_config.get('scope')
    while True:
        scope = input("Scope -> ")
        for temp_scope in constraints:
            if temp_scope == scope:
                return scope
        print("Invalid scope, available options:")
        for temp_scope in constraints:
            print("{}{}".format(" -> ", temp_scope))


def get_uid():
    constraints = config.user_config.get('input_validation')
    while True:
        uid = input("UID -> ")
        if int(constraints.get('uid').get('maxLength')) > len(uid) \
                > int(constraints.get('uid').get('minLength')):
            return uid
        else:
            print("UID should be of maximum length {} and minimum length {}"
                  .format(constraints.get('uid').get('maxLength'),
                          constraints.get('uid').get('minLength')))


def get_name():
    constraints = config.user_config.get('input_validation')
    while True:
        name = input("Name -> ")
        if int(constraints.get('name').get('maxLength')) > len(name) \
                > int(constraints.get('name').get('minLength')) \
                and name.isalpha():
            return name
        else:
            print("Name should be of minimum length {} and maximum length {} and contain only alphabets"
                  .format(constraints.get('uid').get('minLength'),
                          constraints.get('uid').get('maxLength')))


def get_password():
    constraints = config.user_config.get('input_validation')
    while True:
        password = input("Password -> ")
        if int(constraints.get('password').get('maxLength')) > len(password) \
                > int(constraints.get('password').get('minLength')) \
                and password.isalnum():
            return str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10)), 'utf-8')
        else:
            print("Password should be of minimum length {} and maximum length {} and contain numbers as "
                  "well as alphabets"
                  .format(constraints.get('password').get('minLength'),
                          constraints.get('password').get('maxLength')))


def get_gender():
    while True:
        gender = input("Gender (male/female) -> ")
        if gender == 'm' or gender == 'F' or gender.upper() == 'MALE':
            return 'male'
        elif gender == 'f' or gender == 'F' or gender.upper() == 'FEMALE':
            return 'female'
        else:
            print("Invalid input, try again")


def get_phone_number():
    constraints = config.user_config.get('input_validation')
    while True:
        password = input("Phone Number -> ")
        if int(constraints.get('phoneNumber').get('length')) is len(password) and password.isnumeric():
            return password
        else:
            print("Password should be of length {} and contain only numbers"
                  .format(constraints.get('phoneNumber').get('length')))
