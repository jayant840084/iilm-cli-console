from cliConsole import db

collection = db.get_db()['users']


def add_user(user_data):
    return collection.insert_one(user_data)


def find_by_uid(uid):
    return collection.find_one({'uid': uid})


def update_password(uid, password):
    return collection.update_one({
        'uid': uid
    }, {
        '$set': {
            'password': password
        }
    }, upsert=False)
