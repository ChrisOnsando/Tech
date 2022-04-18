from re import A
import numpy as np

def my_array():
    z = np.array(["1, 435, 56633, 2400, 868"])
    return(z)
my_array()

def month():
    my_month = np.busday_count('2011', '2012')

    return(my_month)

month()