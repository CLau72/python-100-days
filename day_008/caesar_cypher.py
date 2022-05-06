#!/usr/bin/env python3

# Caesar Cipher Encrypt/Decrypt
# Prompt for encrypt or decrypt
# Take input word
# Shift alphabet based on an integer shift value

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


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
    print(''.join(encrypted_letters))
