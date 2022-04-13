# Write a Python program to check if a given positive integer is a power of four.
from math import log, floor
from re import X

def checkPowerOf4(n):
    X = log(n) / log(4)
    return X == floor(X)
 
n = 220
 
if checkPowerOf4(n):
        print(n, 'is a power of 4')
else:
        print(n, 'is not a power of 4')