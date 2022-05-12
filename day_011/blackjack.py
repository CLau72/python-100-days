#!/usr/bin/env python3

# Blackjack
# You and the dealer get 2 cards and try to reach 21 without going over.
from art import logo
import random
import os

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Clear Screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return('  ')

# Append a new card value to the input player
def deal_card(deal_player):
    deal_player.append(random.choice(deck))
    return deal_player

# Calculate the score of an input hand
def calc_score(hand):
    score = sum(hand)
    if len(hand) == 2 and score == 21:
        #Zero score denotes blackjack
        score == 0
    elif 11 in hand and score > 21:
        score -= 10
    return score


def compare_score(player_final, computer_final):
    if player_final == 0:
        return 'You win! Blackjack!'
    elif player_final > 21:
        return 'Bustin\' does not make me feel good'
    elif computer_final > 21:
        return 'Computer busts. You win!'
    elif player_final > computer_final:
        return 'You win!'
    elif player_final < computer_final:
        return 'You lose'
    elif player_final == computer_final:
        return 'Draw'


# Overall game logic
def blackjack():
    player_game_prompt = input('Do you want to play Blackjack? Type "y" or "n": ')
    
    #initialize game variables
    player_hand = []
    computer_hand = []
    player_busted = False
    game_active = False

    if player_game_prompt == 'y': 
        # Set gamestate to true and deal cards       
        game_active = True
        deal_card(player_hand)
        deal_card(player_hand)
        deal_card(computer_hand)
        deal_card(computer_hand)
    # clear the screen and print the logo
    clear()
    print(logo)

    # Main game logic loop
    while game_active == True:
        
        # Calculate initial scores:
        player_score = calc_score(player_hand)
        computer_score = calc_score(computer_hand)
        # set to true if busted to bypass a lot of the extra logic
        if player_score > 21:
            player_busted = True

        print(f'    Your cards: {player_hand}, current score: {player_score}' )
        print(f'    Computer\'s first card: {computer_hand[0]}')

        if not player_busted:
            draw = input('Type "y" to get another card, type "n" to pass: ')

        if draw == 'y' and not player_busted:
            deal_card(player_hand)
        elif draw == 'n' or player_busted:
            while computer_score <= 17:
                print(f'    Computer\'s final hand: {computer_hand}, final score: {player_score}' )
                deal_card(computer_hand)
                computer_score = calc_score(computer_hand)
            print(f'    Your final hand: {player_hand}, final score: {player_score}' )
            print(f'    Computer\'s final hand: {computer_hand}, final score: {computer_score}' )
            print(compare_score(player_score, computer_score))
            blackjack()


blackjack()