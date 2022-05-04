#This GUI app is Currently in Development.
from cProfile import label
from logging import root
from tkinter import *
import requests
import json

top = Tk()
# Currency converter title
top.title("CURRENCY CONVERTER")
# Currency converter dimensions height,width
top.geometry("450x300")
class Currency_convertor:
# An empty dict to store the conversion rates.

    rates = {} 

def __init__(self, url):
        data = requests.get(url).json()
  
# Extracting only the rates from the json data.

        self.rates = data["rates"] 
  
# A function to do a simple cross multiplication between the amount and the conversion rates.

def convert_currency(self, from_currency, to_currency, amount):

        initial_amount = amount
  
        amount = amount / self.rates[from_currency]
  
        amount = round(amount * self.rates[to_currency])

        #print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

	
# the label for from_currency
from_currency = Label(top,
				text = "From Currency").place(x = 40,
										y = 60)
	
# the label for to_currency
to_currency = Label(top,
					text = "To Currency").place(x = 40,
											y = 100)

amount_converted = Label(top,
					text = "Amount Converted").place(x = 40,
											y = 150)
	                                            
	
convert_button = Button(top,
					text = "Convert").place(x = 40,
											y = 180)

exit_button = Button(top, text = "EXIT PROGRAM", width=17, command=top.quit)
exit_button.pack()
		
from_currency_input_area = Entry(top,
							width = 20).place(x = 150,
											y = 60)
	
to_currency_entry_area = Entry(top,
								width = 20).place(x = 150,
												y = 100)
amount_converted_entry_area = Entry(top,
								width = 20).place(x = 173,
												y = 150)
		
if __name__ == "__main__":
  
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', "0cb31eb76a29258a165f5e10a7eb79dd")  
  
    c = Currency_convertor()



top.mainloop()