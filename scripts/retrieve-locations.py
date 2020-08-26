import requests
import json

url = "https://api.openaq.org/v1/locations?page={}"
data = []

for i in range(125):
    urlformat = url.format(i)
    print(urlformat)
    r = requests.get(urlformat)
    data.append(r.json())

with open('locations.json', 'w') as data_file:
    json.dump(data, data_file)