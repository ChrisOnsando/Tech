#Write a python function to find the length of the last word
def length_last_word(A):
    arr=A.split(' ')
    size=len(arr)
    if(size==1):
        return len(A)

    last_word=arr[-1]
    return last_word

A="HelloWorld"
print(length_last_word(A))

#Write a python program to remove duplicates from list
data = ['a', 'b', 'c', 'd', 'a', 'd', 10, 20, 30, 40, 10, 20]
print(list(dict.fromkeys(data)))

#Write a python program to read a given CSV file as a dictionary


#Write a password generator function 
import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_?/"
length_password = int(input("Enter Password Length:"))
x = "".join(random.sample(password,length_password))
print(f"Your Random Password is:{x}")

#Given a year, determine whether it is a leap year. If it is a leap year return the boolean true otherwise return false
def CheckLeap(Year):   
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("True") 
  else:  
    print ("False")   
Year = int(input("Enter the Year to check: "))   
CheckLeap(Year)  
