# A Python program to check if a number is a perfect square.
import math
from math import sqrt

def perfect_square():
    number = int(input("Enter the Number:"))

    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return(number, "is a perfect square")
    else:
        return(number, "is not a perfect square")
perfect_square()