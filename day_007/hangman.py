#!/usr/bin/env python3

# This program will be for playing hangman. The basic logic will be:
# Step 1: Select a random word from a word list
# Step 2: Get the length of the word to generate blanks
# Step 3: Prompt User for letter input
# Step 4: Put letters in answer or lose life based on answer
# Step 5: Repeat 4-5 until either you win or die

import os
import random
import hangman_art
import hangman_wordlist

# Import art from the hangman_art module and set it to the art variable
art = hangman_art.stages

# Import wordlist from the hangman_wordlist module and set it to the word_list variable
word_list = hangman_wordlist.word_list

# Randomly select a word from the list
selected_word = random.choice(word_list)
solution = list('_' * len(selected_word))

#  Set lives based on the ASCII art array
lives = len(art) - 1

# Initialize a set to show already guessed letters
guessed_letters = set()

# This function is used to clear and re-draw the screen after each guess
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return('  ')

clear()
print(hangman_art.logo + '\n')

# Loop the game while blanks exist in the solution or player still has lives
while '_' in solution and lives > 0:
    # Clear the screen Print the current state of the solution
    # Also print the art based on how many lives are left
    print(' '.join(solution))
    print(art[lives])

    # This will hide the guessed letters prompt until the first guess
    if guessed_letters:
        print(f'Guessed Letters: {guessed_letters}')

    # Prompt player for a letter input
    letter_choice = input('Select a letter:\n').lower()
    clear()
    # Check if the letter is in the word or not
    if letter_choice in selected_word:
        # If the letter is in the word, loop through and fill in the blanks of the solution list
        for letter in range(0, len(selected_word)):
            if letter_choice == selected_word[letter]:
                solution[letter] = letter_choice
    # If the letter isn't in the word, and hasn't been guessed previously remove a life
    elif letter_choice not in guessed_letters:
        lives -= 1

    # Add the letter choice to the guessed letters set after the letter has been evaluated 
    guessed_letters.add(letter_choice)

# After escaping the loop, clear teh screen then draw the win or lose condition
clear()
if '_' not in solution:
    print(f'\nThe word was {selected_word}')
    print(
        '''
        🤠
        /|👍
        / \\
        '''
    )
    print('You Win!')

else:
    print(f'\nThe word was {selected_word}')
    print(art[0])
    print('You Lose!')
