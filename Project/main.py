# Import the modules needed
from locale import currency
import requests
  
class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {} 
    def __init__(self, url):
        data = requests.get(url).json()
  
        # Extracting only the rates from the json data
        self.rates = data["rates"] 
  
    # function to do a simple cross multiplication between 
    # the amount and the conversion rate
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        #if from_currency != 'EUR' :
        amount = amount / self.rates[from_currency]
  
        amount = round(amount * self.rates[to_currency])
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
  
if __name__ == "__main__":
  
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', "0cb31eb76a29258a165f5e10a7eb79dd")  
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))
  
    c.convert(from_country, to_country, amount)