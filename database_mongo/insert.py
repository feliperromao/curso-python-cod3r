from conexao import db
import datetime

def insertOne(collection, data):
    myCollection = db[collection]
    data.update({'created_at', datetime.datetime.now()})
    return myCollection.insert_one(data).inserted_id
