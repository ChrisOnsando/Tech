# A Python program to find the maximum and minimum values in a given list of tuples using a lambda function.
def max_min():
    list = [(4,10),(5,6),(9,11),(3,1),(0,1)]
    find_max = max(list,key=lambda item:item[1])[1]
    find_min = min(list,key=lambda item:item[1])[1]
    print("Maximum and minimum values are:",find_max,find_min)

max_min()