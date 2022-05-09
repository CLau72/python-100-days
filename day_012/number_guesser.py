#!/usr/bin/env python3

# Import the art and the random functions
from art import logo
import random

# Set constants for difficulties 
EASY_GUESSES = 10
HARD_GUESSES = 5

# Game Function
def number_guesser(difficulty):

    # Select random number
    answer = random.randint(1,100)

    # Set number of guesses based on input an set gamestate 
    if difficulty == 'easy':
        guesses = EASY_GUESSES
        game_active = True
    elif difficulty == 'hard':
        guesses = HARD_GUESSES
        game_active = True
    else:
        print('Invalid selection')
        game_active = False

    # While game state is active, loop through asking for guesses
    while guesses > 0 and game_active == True:
        print(f'You have {guesses} guesses remaining.')
        guess = int(input('Make a guess: '))
        
        if guess == answer:
            print(f"Correct! Answer was {answer}")
            game_active = False
        elif guess > answer:
            print('Too High!')
            guesses -=1
        elif guess < answer:
            print('Too Low!')
            guesses -=1

        
print(logo)
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number_guesser(difficulty)