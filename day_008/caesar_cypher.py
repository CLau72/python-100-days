#!/usr/bin/env python3

# Caesar Cipher Encrypt/Decrypt
# Prompt for encrypt or decrypt
# Take input word
# Shift alphabet based on an integer shift value

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Overall caesar function
def caesar(direction, message, shift_value):

    output_letters = []
    # Account for shift numbers > 26
    shift_value = shift_value % 26

    for letter in message:
        if letter in alphabet:
            if direction == 'encode':
                letter_index = alphabet.index(letter) + shift_value
                # if the index goes outside the range of the alphabet, subtract to come back to start of alphabet
                if letter_index >= len(alphabet):
                    letter_index -= len(alphabet)
            elif direction == 'decode':
                letter_index = alphabet.index(letter) - shift_value
            output_letters.append(alphabet[letter_index])
        # If character isn't a letter, just append the letter
        else:
            output_letters.append(letter)
    
    print(''.join(output_letters))

# recursive function to restart the program based on prompt.
# If user wants to restart the program, prompt for new inputs and call the caesar function
# after encoding/decoding, call restart again
def restart():
    again = input('\nRestart program? (y/n)\n').lower()
    if again == 'y':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
        restart()

caesar(direction, text, shift)
restart()