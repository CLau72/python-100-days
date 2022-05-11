#!/usr/bin/env python3

import art
import game_data
import os
import random


# Get random account from list
def select_account():
    return random.choice(game_data.data)

# Check if the guess is correct
def check_guess(guess, a_followers, b_followers):
    if guess == 'a' and a_followers > b_followers:
        return True
    elif guess == 'b' and b_followers > a_followers:
        return True
    else:
        return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return('  ')

# TODO Repeat game while user is answering correctly.
def game():

    # Initialize score, set game state to True, and generate a random value for A
    score = 0
    game_active = True
    option_a = select_account()

    
    while game_active == True:
        clear()
        print(art.logo)

        # Condition to display current score
        if score > 0:
            print(f"You're Right! Current score: {score}")

        # Select a value for option B, if option_b == option_a, reselect option_b
        # Used while loop in case the same account was randomly selected more than once
        option_b = select_account()
        while option_a == option_b:
            option_b = select_account()

        # Show matchup
        print(f"Compare A: {option_a['name']} a {option_a['description']} from {option_a['country']}")
        print(art.vs)
        print(f"Against B: {option_b['name']} a {option_b['description']} from {option_b['country']}")

        # Prompt user for guess
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if guess is corrected. 
        # If yes, add point and move option_b to option_a
        # If no, set the game state to false
        if check_guess(user_guess, option_a['follower_count'], option_b['follower_count']) == True:
            score += 1
            option_a = option_b
        else:
            game_active = False
    clear()
    print(art.logo)
    print(f"Sorry. That's incorrect. Final score: {score}")
    
game()