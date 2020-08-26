import schedule
import time
import requests
import json
import pprint
import pymongo

url = "https://api.openaq.org/v1/countries"
client = pymongo.MongoClient("mongodb+srv://society:7SFmyyvkbzxFHcd@cluster0.6vxzf.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]
col = db["pokemons"]

def job():
    x = col.find_one()
    print(x)
    # r = requests.get(url)
    # pprint.pprint(r.json())

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)