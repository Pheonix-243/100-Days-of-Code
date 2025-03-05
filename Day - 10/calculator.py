# ---------------- Day 10 Project: Calculator ----------------

# ASCII Art for Calculator Logo
logo = """
 _____________________
|  _________________  |
| | Python Calc    | |  
| |_________________| |  
|  ___ ___ ___   ___  |  
| | 7 | 8 | 9 | | + | |  
| |___|___|___| |___| |  
| | 4 | 5 | 6 | | - | |  
| |___|___|___| |___| |  
| | 1 | 2 | 3 | | x | |  
| |___|___|___| |___| |  
| | . | 0 | = | | / | |  
| |___|___|___| |___| |  
|_____________________|
"""

# Calculator Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Calculator Function
def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))

    while True:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation: ")
        num2 = float(input("Enter next number: "))

        calculation_function = operations[operation]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {int(result)}")

        continue_calc = input("Type 'y' to continue with this result, or 'n' to start a new calculation: ").lower()
        if continue_calc == "y":
            num1 = result
        else:
            break

calculator()
