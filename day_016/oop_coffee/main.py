from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    user_input = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_input == 'off':
        machine_on = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_input):
        order = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(order):
            price = order.cost
            if money_machine.make_payment(price):
                coffee_maker.make_coffee(order)

