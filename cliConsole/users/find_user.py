from cliConsole.utils import utils_print, utils_input, utils_db


def init():
    while True:
        print("Query Type:")
        print("[1] UID")
        print("[2] Name")
        print("[3] Branch")
        query_type = input(">> ")

        if query_type is '1':
            find_by_uid()


def find_by_uid():
    uid = utils_input.get_uid()
    result = utils_db.find_by_uid(uid)
    utils_print.pprint(result)


def find_by_name():
    name = utils_input.get_name()
    result = utils_db
    utils_print.pprint(result)