import requests

from requests.exceptions import Timeout
url = "https://uda.ke/site/"
def timeout_request(url):
    try:
        data = requests.get(url, timeout=10)
        return data.status_code
    except Timeout:
        print('Timeout has been raised.')

print(timeout_request(url))   