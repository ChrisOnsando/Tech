import random

computers_choice = random.choice(['scissors', 'rock', 'paper'])

users_choice = input('Do you want to do- rock, paper or scissors? \n')

if computers_choice == users_choice:
    print('YOU TIE, The COMPUTER HAD CHOSEN ' +computers_choice)

elif users_choice == 'rock' and computers_choice == 'scissors':
    print('YOU WIN, THE COMPUTER HAD CHOSEN ' +computers_choice)

elif users_choice == 'paper' and computers_choice == 'rock':
    print('YOU WIN, THE COMPUTER HAD CHOSEN ' +computers_choice)    

elif users_choice == 'scissors' and computers_choice == 'paper':
    print('YOU WIN, THE COMPUTER HAD CHOSEN ' +computers_choice)

else:
    print('NOW YOU LOSE :( COMPUTER WINS IT')