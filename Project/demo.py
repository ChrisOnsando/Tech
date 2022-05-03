#This GUI app is Currently in Development.
from cProfile import label
from logging import root
from tkinter import *
import requests
from urllib.request import urlopen
import json
root = Tk()
# Currency converter title
root.title("CURRENCY CONVERTER")
# Currency converter dimensions height,width
root.geometry("600x400")

class Currency_convertor:
# An empty dict to store the conversion rates.

    rates = {} 

def __init__(self,url):
    self.url = url
    try:
        data = requests.get(url).json()
        response = urlopen(url)
        data_json = json.loads(response.read())
        data_dict = dict(data_json)
        self.data =data_dict['rates']
    except:
        raise ConnectionError ("Response cannot be retrieved")  

# Extracting only the rates from the json data.

    self.rates = data["rates"] 
  

e1 = Label(root, text="From Currency")
e1.pack()
e1 = Entry(root, bd =5)
e1.pack()
e1.pack()

e2 = Label(root, text="To Currency")
e2.pack()
e2 = Entry(root, bd =5)
e2.pack()
e2.pack()

e3 = Label(root, text="Amount")
e3.pack()
e3 = Entry(root, bd =5)
e3.pack()
e3.pack()


def myClick():
    myclick =label(root)
    myclick.pack()

myButton = Button(root, text = "CONVERT", width=17, command=myClick)
myButton.pack()

button_exit = Button(root, text = "EXIT PROGRAM", width=17, command=root.quit)
button_exit.pack()

if __name__ == "__main__":
  
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', "0cb31eb76a29258a165f5e10a7eb79dd")  

    
root.mainloop()