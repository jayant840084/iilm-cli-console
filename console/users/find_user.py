from console.utils import utils_print, utils_input, utils_db


def init():
    while True:
        print("[0] Return To Previous Menu")
        print("[1] Find By UID")
        # print("[2] Find By Name")
        # print("[3] Find By Branch")
        query_type = input(">> ")
        if query_type is '0':
            return
        elif query_type is '1':
            find_by_uid()
        else:
            print("Invalid choice, try again")


def find_by_uid():
    uid = utils_input.get_uid()
    result = utils_db.find_by_uid(uid)
    utils_print.pprint(result)


def find_by_name():
    name = utils_input.get_name()
    # result = utils_db
    # utils_print.pprint(result)
