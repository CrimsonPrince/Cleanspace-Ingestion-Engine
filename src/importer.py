import ndjson
import pprint
import pymongo

client = pymongo.MongoClient("mongodb://fyp:KH9jYNsWsCiaUv@54.74.63.10")
db = client["fyp"]
col = db["Measurements"]
insertList = []


def importFileToMongo():

    with open('realtime/2020-08-27/1598487787.ndjson') as f:
        data = ndjson.load(f)
    col.insert_many(data)
importFileToMongo()