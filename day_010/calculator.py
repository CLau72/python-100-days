#!/usr/bin/env python3

# Calculator

from art import logo
import os

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def mult(n1, n2):
    return n1 * n2

# Divide
def div(n1, n2):
    return n1 / n2

# Clear Screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return('  ')

# Dictionary that references the functions by their symbols
operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
}

def calculator():
    print(logo)

    num1 = float(input('What is the first number?: '))
    for operation in operations:
        print(operation)
    operation_symbol = input("Pick an operation from the lines above: ")
    num2 = float(input('What is the second number?: '))

    answer = operations[operation_symbol](num1, num2)


    print(f'{num1} {operation_symbol} {num2} = {answer}')

    continue_operation = True

    while continue_operation == True:
        continue_prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start with a new number.: ")
        if continue_prompt == 'n':
            continue_operation = False
        else:
            num3 = answer
            operation_symbol = input("Pick an operation: ")
            num4 = float(input("What's the next number? "))
            answer = operations[operation_symbol](num3, num4)
            print(f'{num3} {operation_symbol} {num4} = {answer}')
    clear()
    calculator()
calculator()