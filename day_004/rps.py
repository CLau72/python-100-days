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


rps_list = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
comp_choice = random.randint(0,2)

if user_choice >= 0 and user_choice <= 2:
    print(f'You selected:\n {rps_list[user_choice]}\n')
    print(f'Computer selected:\n {rps_list[comp_choice]}\n')
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
else:
    print('Invalid selection. Exiting game.')