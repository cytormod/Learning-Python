from cloudinit.util import multi_log

from store import MENU, resources
#
#
# is_available = True
#
# def extract_ingredients(type_of_coffee):
#     return MENU[type_of_coffee]["ingredients"]
#
# def calculating_resources():
#     """Here we are calculating the resources in our store"""
#     espresso_water = extract_ingredients('espresso')
#     print(espresso_water['water'])
#
# calculating_resources()
#
# extract_ingredients("espresso")
# while is_available:
#     choice = input("What would you like? (espresso/latte/cappuccino):")
#     if choice == 'espresso':
#         espresso_ing = extract_ingredients('espresso')
#         print(espresso_ing)
#     elif choice == "off":
#         is_available = False
#     elif choice == 'report':
#         print(resources)

profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?: ")) *0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) *0.05
    total += int(input("how many pennies?: ")) *0.25
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"$:{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink['ingredients'])