#!/usr/bin/env python3

import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])


user_choice = input('Do you want - rock, paper or scissors?\n')

if computer_choice == user_choice: 
    print("It's a TIE")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You WIN, The Computer had ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You WIN, The Computer had ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You WIN, The Computer had '  + computer_choice)

else:
    print('You Lose Computer had ' + computer_choice )
