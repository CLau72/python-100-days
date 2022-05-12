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
        score = 0
    elif 11 in hand and score > 21:
        score -= 10
        hand.remove(11)
        hand.append(1)
    return score


def compare_score(player_final, computer_final):
    if player_final == 0:
        return 'You win! Blackjack!'
    elif computer_final == 0:
        return 'Bad Luck. Dealer Blackjack'
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


def blackjack():
    player_game_prompt = input('Do you want to play Blackjack? Type "y" or "n": ')
<<<<<<< HEAD
    
    #initialize game variables
=======

>>>>>>> ce80a45123762c289a2c9527f07273bca985433c
    player_hand = []
    computer_hand = []
    game_active = False
<<<<<<< HEAD

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
=======
    
    if player_game_prompt == 'y':
        clear()
        print(logo)
        game_active = True

        for _ in range(2):
>>>>>>> ce80a45123762c289a2c9527f07273bca985433c
            deal_card(player_hand)
            deal_card(computer_hand)

        while game_active == True:

            player_score = calc_score(player_hand)
            computer_score = calc_score(computer_hand)


            if player_score == 0 or computer_score == 0 or player_score > 21:
                game_active = False
            else:
                print(f'    Your cards: {player_hand}, current score: {player_score}' )
                print(f'    Computer\'s first card: {computer_hand[0]}')
                draw = input('Type "y" to get another card, type "n" to pass: ')

                if draw == 'y':
                    deal_card(player_hand)
                    player_score = calc_score(player_hand)
                elif draw == 'n':
                    while computer_score <= 17 and compare_score != 0:
                        deal_card(computer_hand)
                        computer_score = calc_score(computer_hand)
                    game_active = False

        print(f'    Your final hand: {player_hand}, final score: {player_score}' )
        print(f'    Computer\'s final hand: {computer_hand}, final score: {computer_score}' )
        print(compare_score(player_score, computer_score))
        blackjack()

blackjack()