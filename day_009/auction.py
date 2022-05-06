#!/usr/bin/env python3

# This program facilitates a silent auction by prompting for a person's name and bid.
# Once all the names and bids have been collected, find the person with the largest bid

import os
from art import logo

# Clear function taken from day 7's hangman project to clear the terminal 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return('  ')

# Takes in dictionary of bids, iterates through it, and finds the highest bid.
def highest_bid(bids):
    highest_bid = 0
    highest_bidder = ''

    for name, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name

    print(f'{highest_bidder} has the highest bid with ${highest_bid}')

bidders = {}
add_bidders = True

print(logo)
print('Welcome to the secret auction program.')

while add_bidders == True:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    bidders[name] = bid

    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == 'no':
        add_bidders = False

    clear()
    
highest_bid(bidders)
