from pymongo import MongoClient
from config import MONGO_URL
from datetime import datetime


# FormsData = FormsCol.find({})
# for Form in FormsData:
#     print(Form)


class Forms:
    def __init__(self):
        cluster = MongoClient(MONGO_URL)
        db = cluster["template_system"]
        FormsCol = db["Forms"]
        self.Coll = FormsCol

    def getAllData(self):
        return self.Coll.find({})

    def addData(self, name, email):
        form = {
            "name": name,
            "email": email,
            "subscribe": True,
            "subscribe_time":  datetime.now(),
            "unsubscribe_time":  datetime.now(),
        }
        self.Coll.insert_one(form)

    
