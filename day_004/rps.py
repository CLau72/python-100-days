#!/usr/bin/env python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Placing the provided ASCII art into a list
rps_list = [rock, paper, scissors]

# Getting the user and computer choices
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
comp_choice = random.randint(0,2)

# Checking to make sure the entered value is valid
if user_choice >= 0 and user_choice <= 2:

    # Printing the user choice and computer choice ASCII art
    print(f'You selected:\n {rps_list[user_choice]}\n')
    print(f'Computer selected:\n {rps_list[comp_choice]}\n')

    # Comparing choices to determine the winner
    if user_choice == comp_choice:
        print('DRAW!')
    elif user_choice == 0 and comp_choice == 1:
        print('YOU LOSE!')
    elif user_choice == 0 and comp_choice == 2:
        print('YOU WIN!')
    elif user_choice == 1 and comp_choice == 0:
        print('YOU WIN!')
    elif user_choice == 1 and comp_choice == 2:
        print('YOU LOSE!')
    elif user_choice == 2 and comp_choice == 0:
        print('YOU LOSE')
    elif user_choice == 2 and comp_choice == 1:
        print('YOU WIN!')
        
# Handling the case where an invalid selection is made
else:
    print('Invalid selection. Exiting game.')