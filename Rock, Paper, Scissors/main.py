import random

computers_choice = random.choice(['scissors', 'rock', 'paper'])

users_choice = input('Do you want to do- rock, paper or scissors? \n')

if computers_choice == users_choice:
    print('TIE')

elif users_choice == 'rock' and computers_choice == 'scissors':
    print('WIN')

elif users_choice == 'paper' and computers_choice == 'rock':
    print('WIN')    

elif users_choice == 'scissors' and computers_choice == 'paper':
    print('WIN')

else:
    print('You Lose :( Computer Wins')