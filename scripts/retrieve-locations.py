import requests
import json
import pprint
from datetime import datetime

url = "https://api.openaq.org/v1/locations"
response = []
cities = []
date_time_str = '2018-06-29 08:15:27'
date_time_obj = datetime.fromisoformat(date_time_str) 

r = requests.get(url)
response.append(r.json())
response = response[0]['results']
response[:] = (n for n in response if datetime.strptime(n['lastUpdated'], '%Y-%m-%dT%H:%M:%Sz') < date_time_obj)
pprint.pprint(response)

with open('cities.json', 'w') as data_file:
    json.dump(response, data_file)