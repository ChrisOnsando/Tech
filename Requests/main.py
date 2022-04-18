from re import X
import requests

x = requests.get('https://www.google.com')
print(x.text)

x = requests.head('https://www.google.com')
print(x.text)

x = requests.delete('https://www.google.com')
print(x.text)

x = requests.post('https://www.google.com')
print(x.text)

x = requests.patch('https://www.google.com')
print(x.text)

x = requests.put('https://www.google.com')
print(x.text)