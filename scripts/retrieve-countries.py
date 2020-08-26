import requests
import json
import pprint

url = "https://api.openaq.org/v1/countries"
response = []
cities = []

r = requests.get(url)
response.append(r.json())
response = response[0]['results']
response[:] = (n for n in response if n['cities'] >= 20)
pprint.pprint(response)

with open('cities.json', 'w') as data_file:
    json.dump(response, data_file)