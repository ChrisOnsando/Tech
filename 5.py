#Write a python program to remove duplicates from list
data = ['a', 'b', 'c', 'd', 'a', 'd', 10, 20, 30, 40, 10, 20]
print(list(dict.fromkeys(data)))