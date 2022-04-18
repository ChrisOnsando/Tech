import random
from re import M
print(random.randrange(1, 100))

# Random seed() Method

random.seed(10)
print(random.random())

# Random choice() Method
MyList = ["Nairobi", "Kisumu", "Eldoret"]
print(random.choice(MyList))

# Random choices() Method
my_list = ["Nairobi", "Kisumu", "Eldoret"]
print(random.choices(my_list, weights = [4, 2, 2], k = 10))

# Random sample() Method
myList = ["Nairobi", "Kisumu", "Eldoret"]
print(random.sample(myList, k = 3))

# Random shuffle() Method
mylist = ["Nairobi", "Kisumu", "Eldoret"]
random.shuffle(mylist)
print(mylist)