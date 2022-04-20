import requests
def get_requests():
    r = requests.get('https://www.google.com/')
    print(r.text)
    return(r.content)
get_requests()
