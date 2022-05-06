#!/usr/bin/env python3

# Caesar Cipher Encrypt/Decrypt
# Prompt for encrypt or decrypt
# Take input word
# Shift alphabet based on an integer shift value

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Overall caesar function
def caesar(direction, message, shift_value):

    output_letters = []
    for letter in message:
        if direction == 'encode':
            letter_index = alphabet.index(letter) + shift
            # if the index goes outside the range of the alphabet, subtract to come back to start of alphabet
            if letter_index >= len(alphabet):
                letter_index -= len(alphabet)
        elif direction == 'decode':
            letter_index = alphabet.index(letter) - shift
        output_letters.append(alphabet[letter_index])
    
    print(''.join(output_letters))

run_program = True

# Loop the program until a user states they don't want to restart
while run_program:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    
    restart = input('Would you like restart? (y/n)\n').lower()
    if restart == 'n':
        run_program = False