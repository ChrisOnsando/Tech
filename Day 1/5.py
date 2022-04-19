# A python program to remove duplicates from list
def my_duplicate():
    data = ['a', 'b', 'c', 'd', 'a', 'd', 10, 20, 30, 40, 10, 20, 30, 40]
    print(list(dict.fromkeys(data)))

my_duplicate()

def my_function(x):
    return list(dict.fromkeys(x))
my_list = my_function(["a", "b", "a", "b", "b", "a", "c", "c", "d"])
print(my_list)