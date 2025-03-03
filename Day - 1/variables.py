# ===================================
# PYTHON VARIABLES & NAMING RULES
# ===================================

# In Python, variables are used to store data. Unlike some other languages,
# Python variables do not require explicit declaration of their data types.

# Assigning values to variables
name = "Bright"       # String
age = 22             # Integer
height = 1.75        # Float
is_student = True    # Boolean

# Python is dynamically typed, meaning variables can change types.
age = "twenty-two"   # Now it's a string instead of an integer.

# ===================================
# VARIABLE NAMING RULES
# ===================================

# 1. Variables can contain letters, numbers, and underscores.
valid_variable = "Yes"
another_valid123 = "Sure"
_valid_name = "Okay"

# 2. Variables CANNOT start with a number.
# 123name = "Wrong"  ❌ (SyntaxError)

# 3. Variables CANNOT contain spaces.
# my variable = "No"  ❌ (SyntaxError)

# 4. Variables are case-sensitive.
Number = 10
number = 5
print(Number, number)  # Output: 10 5

# 5. Reserved keywords cannot be used as variable names.
# if = 5  ❌ (SyntaxError)
# class = "OOP" ❌ (SyntaxError)

# 6. Use descriptive variable names for readability.
user_age = 30  # ✅ (Good)
x = 30         # ❌ (Not descriptive)

# 7. Use snake_case (underscore-separated) for variable names in Python.
first_name = "Bright"  # ✅ (Recommended)
firstName = "Bright"   # ✅ (Works, but not Pythonic)

# 8. Constants (values that shouldn't change) are typically written in ALL_CAPS.
PI = 3.14159  # ✅ (Convention for constants)

# ===================================
# VARIABLE SCOPE
# ===================================

# Python variables can be local or global.
global_variable = "I am global"  # This can be accessed anywhere in the script.

def example_function():
    local_variable = "I am local"  # Only accessible inside this function.
    print(local_variable)

example_function()
# print(local_variable)  # ❌ (This would cause an error)

# ===================================
# MULTIPLE VARIABLE ASSIGNMENT
# ===================================

a, b, c = 10, 20, 30  # Assigning multiple values in one line
print(a, b, c)  # Output: 10 20 30

x = y = z = "Same value"  # Assigning the same value to multiple variables
print(x, y, z)  # Output: Same value Same value Same value

# ===================================
# DELETING VARIABLES
# ===================================
temp = "This is temporary"
del temp  # The variable is now deleted and cannot be used anymore.
# print(temp)  # ❌ (This would cause an error)

# ===================================
# SUMMARY
# ===================================
# - Variables store data.
# - Naming rules: No spaces, no starting with numbers, case-sensitive.
# - Use descriptive names and snake_case.
# - Constants are written in ALL_CAPS.
# - Variables can be local or global.
# - You can assign multiple variables at once.
# - Variables can be deleted using `del`.
