from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
menu.menu

option_1 = input("What would you like to have (espresso, latte, cuppaccino) : ").lower()

menu_item = menu.find_drink(option_1)

money_machine = MoneyMachine()

if option_1 == "report":
    coffee_maker.report()
elif option_1 != "report":
    if menu_item is not None:
        print(f"The cost of {menu_item.name} is ${menu_item.cost}.")
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
        else:
            print("Sorry, out of resources")
    else:
        print("Invalid option. Please choose a valid drink from the menu.")
