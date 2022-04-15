# A numpy program to create an array with atleast 5 user input integers and determine the size of the memory occupied by the arrray
import numpy as np
def my_array():
    z = np.array(["1, 435, 56633, 2400, 868"])
    print("Array:")
    print(z)
    print("Size of memory occupied by array:")
    print("%d bytes" % (z.size * z.itemsize))

my_array()
