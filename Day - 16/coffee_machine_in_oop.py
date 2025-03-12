# ---------------- Day 16 Project: Coffee Machine with OOP ----------------

class CoffeeMachine:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
        self.menu = {
            "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
            "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
            "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']}")

    def is_resource_sufficient(self, order):
        for item in self.menu[order]["ingredients"]:
            if self.menu[order]["ingredients"][item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickels?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return total

    def make_coffee(self, order):
        for item in self.menu[order]["ingredients"]:
            self.resources[item] -= self.menu[order]["ingredients"][item]
        print(f"Here is your {order} ☕. Enjoy!")

    def run(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                print("Turning off the coffee machine. Goodbye!")
                break
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                if self.is_resource_sufficient(choice):
                    payment = self.process_coins()
                    cost = self.menu[choice]["cost"]
                    if payment >= cost:
                        change = round(payment - cost, 2)
                        print(f"Here is ${change} in change.")
                        self.resources["money"] += cost
                        self.make_coffee(choice)
                    else:
                        print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Invalid selection. Please choose again.")

# Start the coffee machine
toffee_machine = CoffeeMachine()
toffee_machine.run()
