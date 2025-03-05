# Day 12: Scope & Namespaces

# 1. Local Scope
# Variables created inside a function exist only within that function.
def local_function():
    local_var = 10  # Local variable
    print(local_var)


# print(local_var)  # ❌ This will cause an error because local_var is not accessible outside the function

# 2. Global Scope
# Variables created outside functions exist in the global scope.
global_var = 20


def access_global():
    print(global_var)  # ✅ Accessible inside the function


access_global()


# 3. Modifying Global Variables Inside Functions
# Using the 'global' keyword allows us to modify global variables inside functions.

def modify_global():
    global global_var
    global_var = 30  # Modifying the global variable


modify_global()
print(global_var)  # ✅ Now it prints 30


# 4. Python's LEGB Rule (Local, Enclosing, Global, Built-in)
# Python searches for variables in this order:
# - Local: Inside the current function
# - Enclosing: In any enclosing functions
# - Global: At the top level of the script
# - Built-in: Python's built-in functions and variables

def enclosing_function():
    enclosing_var = 50

    def inner_function():
        print(enclosing_var)  # ✅ Can access enclosing variable

    inner_function()


enclosing_function()

# 5. Using Constants
# Python conventionally uses uppercase names for global constants.
PI = 3.14159  # Constant variable (should not be changed)


# 6. Avoiding Global Variables
# Instead of modifying global variables, it's better to return values and pass them as parameters.
def better_function(x):
    return x + 10


result = better_function(5)
print(result)
