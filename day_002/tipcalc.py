#!/usr/bin/env python3

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to the Tip Calculator')

cost = float(input('How much was the bill? $'))
split = int(input('How many people are splitting it? '))
tip_percent = int(input('10%, 12%, or 15% tip? '))

payment = (cost / split) * (1 + (tip_percent / 100))
payment = round(payment,2)
final_amount = "{:.2f}".format(payment)

print(f'Each person should pay ${final_amount}')