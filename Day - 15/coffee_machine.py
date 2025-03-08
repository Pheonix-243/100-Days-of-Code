# ---------------- Day 15 Project: Coffee Machine ----------------

import os

# Menu and resources
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def is_resource_sufficient(order):
    """Check if there are enough resources to make the order."""
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Ask user for coins and return the total amount."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def make_coffee(order):
    """Deduct ingredients and serve the coffee."""
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]
    print(f"Here is your {order} ☕. Enjoy!")


def coffee_machine():
    """Main function to run the coffee machine program."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        elif choice in MENU:
            if is_resource_sufficient(choice):
                payment = process_coins()
                cost = MENU[choice]["cost"]
                if payment >= cost:
                    change = round(payment - cost, 2)
                    print(f"Here is ${change} in change.")
                    resources["money"] += cost
                    make_coffee(choice)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid selection. Please choose again and again.")
            print("Invalid selection. Please choose again and again.")
            print("Invalid selection. Please choose again and again.")
            print("Invalid selection. Please choose again and again.")
            print("Invalid selection. Please choose again and again.")
            print("Invalid selection. Please choose again and again.")


coffee_machine()
