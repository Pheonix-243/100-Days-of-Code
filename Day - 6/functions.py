# =========================
# Day 6: Python Functions & Karel
# =========================

# A function be a reusable block of code
# We define functions using "def" keyword

def greet():
    """This function prints a greeting message."""
    print("Hello, world!")

greet()  # Calling the function

# ------------------------
# Functions with Parameters
# ------------------------

def greet_name(name):
    """This function greets a specific person."""
    print(f"Hello, {name}!")

greet_name("Bright")  # Output: Hello, Bright!

# ------------------------
# Indentation in Python
# ------------------------

# Python dey use indentation to define blocks of code.
# Wrong indentation go cause error.

# Example of correct indentation:
def say_hello():
    print("Hello!")  # This line be inside the function

say_hello()  # Calling the function
