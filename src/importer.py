import ndjson
import pprint
import pymongo
from pathlib import Path

client = pymongo.MongoClient("mongodb://fyp:KH9jYNsWsCiaUv@54.74.63.10")
db = client["fyp"]
col = db["Measurements"]
insertList = []

def importFileToMongo():

    pathlist = Path("realtime").glob('**/*.ndjson')
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        
        with open(path_in_str) as f:
            data = ndjson.load(f)
            col.insert_many(data)
            print(path_in_str)



importFileToMongo()