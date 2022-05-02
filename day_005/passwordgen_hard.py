#!/usr/bin/python3

#Password Generator Project

# This is the "hard" version of the project.
# It will randomize the order of the 3 types or characters in the password
# The structure is the same as the easy one with an added step of shuffling the character list

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create empty list for characters
password_chars = []

# append characters into list to build up password
for letter in range(1,nr_letters+1):
    password_chars.append(random.choice(letters))
for symbol in range(1,nr_symbols+1):
    password_chars.append(random.choice(symbols))
for number in range(1,nr_numbers+1):
    password_chars.append(random.choice(numbers))

# Shuffle the password_chars list
random.shuffle(password_chars)

# Join chars together to make password string
password = ''.join(password_chars)

print(password)
