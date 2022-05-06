#!/usr/bin/env python3

# Caesar Cipher Encrypt/Decrypt
# Prompt for encrypt or decrypt
# Take input word
# Shift alphabet based on an integer shift value

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function for the encryption process
def encrypt(word, shift):

    # Initialize empty array for letters
    encrypted_letters = []
    # loop through each letter in the input word
    for letter in word:
        # generate a new index based on letter's position in the alphabet + the shift value
        letter_index = alphabet.index(letter) + shift
        # if the index goes outside the range of the alphabet, subtract to come back to start of alphabet
        if letter_index >= len(alphabet):
            letter_index -= len(alphabet)
        # get the shifted letter and append it to the array
        shifted_letter = alphabet[letter_index]
        encrypted_letters.append(shifted_letter)
    print(''.join(encrypted_letters) + '\n')

def decrypt(cipher, shift):

    # Initialize empty array for letters
    decrypted_letters = []
    # loop through each letter in the cipher
    for letter in cipher:
        # generate new index based on letter's position in alphabet - the shift value
        letter_index = alphabet.index(letter) - shift
        # Negative indexes are a thing, so doing math to prevent index error not needed!
        unshifted_letter = alphabet[letter_index]
        decrypted_letters.append(unshifted_letter)
    print(''.join(decrypted_letters) + '\n')


# Overall caesar function
def caesar(direction, message, shift_value):
        # Call the encrypt/decrypt function based on direction input.
        if direction == 'encode':
            encrypt(message, shift_value)
        elif direction == 'decode':
            decrypt(message, shift_value)
        else:
            print('Invalid selection direction selected')


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