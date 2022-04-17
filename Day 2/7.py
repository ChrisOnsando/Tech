import requests
import json

url = 'https://catfact.ninja/facts?limit=1&max_length=140'
def read_data(url):
    response = requests.get(url).text
    dict_data = json.loads(response)
    return dict_data

print(read_data(url))
