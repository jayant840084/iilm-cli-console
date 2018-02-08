import csv, bcrypt, pprint

from cliConsole.utils import utils_db, utils_print

with open('data.csv', newline='') as userFile:
    fieldnames = ['uid', 'email', 'password', 'name', 'gender', 'phoneNumber', 'branch', 'year', 'roomNumber', 'scope']
    userReader = csv.reader(userFile, delimiter=',', quotechar='|')
    for row in userReader:
        user = {}
        user[fieldnames[0]] = row[0]
        user[fieldnames[1]] = row[1]
        user[fieldnames[2]] = str(bcrypt.hashpw(row[2].encode('utf-8'), bcrypt.gensalt(10)), 'utf-8')
        user[fieldnames[3]] = row[3]
        user[fieldnames[4]] = row[4]
        user[fieldnames[5]] = row[5]
        user[fieldnames[6]] = row[6]
        user[fieldnames[7]] = row[7]
        user[fieldnames[8]] = row[8]
        user[fieldnames[9]] = row[9]

        utils_print.pprint(user)

        try:
            db_response = utils_db.add_user(user)
        except:
            pass
