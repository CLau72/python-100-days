#!/usr/bin/env python3

#1. Create a greeting for program

#2. Ask user for the city they grew up in.

#3. Ask user for the name of a pet

#4 Combine the name of their city and pet and show them their bandname

from time import sleep

# Print greeting and wait 2 seconds
print('Welcome to the band name generator!')
sleep(2)

# Prompt for input and save to variables
city = input('What city did you grow up in?\n')
pet = input('What is the name of one of your pets?\n')

# Print out result
print(f'Your band name is {city} {pet}')
input('Press any key to close...')