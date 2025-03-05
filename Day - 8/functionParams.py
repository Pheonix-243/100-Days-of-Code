# Day 8: Functions, Parameters, Arguments, and More!

# 1️⃣ Defining a Function
def greet():
    """This function prints a simple greeting."""
    print("Hello!")
    print("How are you?")
    print("Welcome to Day 8 of Python!")


# Calling the function
greet()


# 2️⃣ Functions with Parameters
def greet_with_name(name):
    """This function takes a name as a parameter and prints a personalized greeting."""
    print(f"Hello, {name}!")
    print(f"How are you today, {name}?")


# Calling the function with an argument
greet_with_name("Angela")


# 3️⃣ Functions with Multiple Parameters
def greet_with_location(name, location):
    """This function takes a name and a location as parameters and prints a greeting."""
    print(f"Hello, {name}!")
    print(f"How is the weather in {location}?")


# Calling the function with arguments
greet_with_location("Bright", "Ghana")


# 4️⃣ Positional vs. Keyword Arguments
# Positional Arguments: Order matters!
def describe_person(name, age):
    """This function describes a person by their name and age."""
    print(f"{name} is {age} years old.")


describe_person("Kwesi", 22)  # Correct
# describe_person(22, "Kwesi")  # Wrong order, doesn't make sense!

# Keyword Arguments: Order does NOT matter!
describe_person(age=22, name="Kwesi")  # Still works fine


# 5️⃣ Default Parameter Values
def greet_with_default(name="Guest"):
    """This function greets a person but has a default value if no name is given."""
    print(f"Hello, {name}!")


greet_with_default()  # Uses default "Guest"
greet_with_default("Bright")  # Overrides default with "Bright"


# 6️⃣ Functions with Return Values
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


result = add(5, 3)
print(f"5 + 3 = {result}")  # Outputs: 5 + 3 = 8


# 7️⃣ Multiple Return Values
def get_full_name(first, last):
    """Returns both first and last name as a tuple."""
    return first, last


full_name = get_full_name("Prophet", "Bright")
print(full_name)  # Outputs: ('Prophet', 'Bright')


# 8️⃣ Using Functions Inside Functions (Nesting)
def outer_function():
    """An example of a function calling another function."""
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()  # Calling the inner function


outer_function()


# 9️⃣ Exercise: Paint Area Calculator
def paint_calc(height, width, cover):
    """Calculates how many cans of paint are needed to cover a wall."""
    area = height * width
    num_cans = (area / cover)
    print(f"You'll need {round(num_cans)} cans of paint.")


# Example usage
paint_calc(height=3, width=5, cover=5)


# 🔟 Prime Number Checker
def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# Testing the prime checker
num = 11
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")
