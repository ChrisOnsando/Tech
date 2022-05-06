my_dict = {num:num**2 for num in range(1,11)}
print(my_dict)

random_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
    }

my_new_dict = {k:v**2 for k,v in random_dict.items()}
print(my_new_dict)

my_new_dict2 = {k:v**2 for k,v in random_dict.items() if v % 2 == 0}
print(my_new_dict2)

my_new_dict3 = {k:v**3 for k,v in random_dict.items() if v % 3 == 0}
print(my_new_dict3)

my_new_dict4 = {k:v**4 for k,v in random_dict.items() if v % 4 == 0}
print(my_new_dict4)

my_new_dict5 = {k:v**5 for k,v in random_dict.items() if v % 5 == 0}
print(my_new_dict5)

my_new_dict6 = {k:v**6 for k,v in random_dict.items() if v % 6 == 0}
print(my_new_dict6)

my_new_dict7 = {k:v**7 for k,v in random_dict.items() if v % 7 == 0}
print(my_new_dict7)

my_new_dict8 = {k:v**8 for k,v in random_dict.items() if v % 8 == 0}
print(my_new_dict8)