#!/usr/bin/env python3

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Contents of the machine by default. Added money to keep track of revenue
resources = {
    "water":300, # default: 300
    "milk": 200, # default: 200
    "coffee": 100, # default: 100
    "money": 0
}

# function to generate a report on current resource values
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


# Check the order to see if the ingredients are available to make the order
def resource_check(order):
    recipe = MENU[order]["ingredients"]
    for resource in recipe:
        if recipe[resource] > resources[resource]:
            print(f'Sorry, there is not enough {resource} to complete your order')
            return False
        else:
            return True

# Sums up inserted coin values
def insert_money():
    print("Please insert coins.")
    quarters = (int(input('How many quarters?: ')) * 0.25)
    dimes = (int(input('How many dimes?: ')) * 0.10)
    nickles = (int(input('How many nickles?: ')) * 0.05)
    pennies = (int(input('How many pennies?: ')) * 0.01)
    return quarters + dimes + nickles + pennies

# Checks if input is sufficient and gives change if over the cost of the drink
def change(input_money, order_cost):
    global resources
    if input_money == order_cost:
        resources["money"] += order_cost
        return True
    elif input_money > order_cost:
        resources["money"] += order_cost
        change = input_money - order_cost
        print(f"Here is ${change:.2f} in change")
        return True
    else:
        print("Insufficient funds")
        return False

# Subtracts the ingredients from the resources dictionary.
def make_drink(order):
    for ingredient in MENU[order]["ingredients"]:
        global resources
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
    print(f"Here is your {order} ☕. Enjoy!")

# Overall function.
def coffee_machine():
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # If user selects a coffee, this will:
    # Check if there are sufficient ingredients 
    # Prompt for money input
    # Give change if necessary
    # Give customer the drink and subtract stored ingredients
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if resource_check(user_input):
            customer_money = insert_money()
            if change(customer_money, MENU[user_input]['cost']):
                make_drink(user_input)
    # Break out of function if shut off
    elif user_input == 'off':
        return
    # Generate resource report
    elif user_input == 'report':
        report()
    # Inform of invalid input
    else:
        print('Invalid input')
    # Repeat opperation
    coffee_machine()

coffee_machine()