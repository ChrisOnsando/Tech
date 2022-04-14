# Write a NumPy program to find the number of weekdays in a given month. Allow user to input the month and year of choice
import numpy as np
my_month = (input('Enter Month(mm): '))

  
my_month = np.busday_count('2011', '2012')

print(my_month)

