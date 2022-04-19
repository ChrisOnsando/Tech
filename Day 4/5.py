# A Python program to generate an infinite cycle of elements from an iterable. The iterable data type should be a list or a string or a dictionary, etc.
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
# A List
result = cycle_data(['A','B','C','D'])
print("This is indefinate:")
for i in result:
    print(i)

# A String
result = cycle_data('Python iterables')
print("This is infinite loop:")
for i in result:
    print(i)