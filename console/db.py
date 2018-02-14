from pymongo import MongoClient


client = MongoClient()

db = client['outpass']


def get_db():
    return db
