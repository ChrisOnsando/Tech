# A password generator function 
import random
def generate_random_password():
    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_?/"
    length_password = int(input("Enter Password Length:"))
    x = "".join(random.sample(password,length_password))
    print(f"Your Random Password is:{x}")
    return(x)
generate_random_password()