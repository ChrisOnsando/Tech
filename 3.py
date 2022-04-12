# Create a Python project to guess a number that has randomly been selected.
import random
def guess_number():
    random_number = random.randint(1,20)
    guess = int(input("Enter number between 1 and 20"))

    if guess < 1 or guess > 20:
        print('Please Guess any number in range')

    elif guess == random_number:
        print('Congratulations! You won')


    