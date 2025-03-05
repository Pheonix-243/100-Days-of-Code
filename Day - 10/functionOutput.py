# ---------------- Day 10 Notes ----------------

# Functions with Outputs
# A function can return a value instead of printing it.
def format_name(f_name, l_name):
    """Takes a first and last name and returns a properly formatted string."""
    if f_name == "" or l_name == "":
        return "Invalid input"
    return f_name.title() + " " + l_name.title()

print(format_name("bright", "appiah"))  # Output: Bright Appiah


# Returning a Boolean
def is_even(number):
    """Checks if a number is even."""
    return number % 2 == 0

print(is_even(10))  # True
print(is_even(7))   # False


# Recursion - A function calling itself
def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# Docstrings - Used to describe a function
def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

print(greet("Bright"))  # Output: Hello, Bright!


# Functions with multiple return values
def get_person_details():
    """Returns multiple values as a tuple."""
    name = "Bright"
    age = 22
    country = "Ghana"
    return name, age, country

details = get_person_details()
print(details)  # Output: ('Bright', 22, 'Ghana')

# Unpacking multiple return values
name, age, country = get_person_details()
print(name)  # Bright
print(age)   # 22
print(country)  # Ghana
