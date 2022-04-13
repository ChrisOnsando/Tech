# Write a Python program to check if a number is a perfect square.
import math
from math import log, floor
from re import X

def perfect_square(number):
    root = math.sqrt(number)
    return int(root + 0.5) ** 2 == number

def check_PowerOf_4(n):
    X = log(n) / log(4)
    return X == floor(X)

