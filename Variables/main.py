x, y, z = "Nemwel", "Junior", "Chris"
print(x, y, z)

x = y = z = "Nemwel Junior Chris"
print(x)
print(y)
print(z)

# Unpack a list

places = ["Nairobi", "Kisumu", "Eldoret"]
x, y, z = places
print(places)
print(x)
print(y)
print(z)

# Using +operator to output multiple variables
x = "Nairobi"
y = "Kisumu"
z = "Eldoret"
print(x + y + z)

# Global Variables
x = "Awesome!"
def MyFunc():
    print("Nairobi is " + x)
MyFunc()