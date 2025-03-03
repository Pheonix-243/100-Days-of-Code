# ==========================
# PYTHON DATA TYPES OVERVIEW
# ==========================

# In Python, everything is an object, and every object has a data type.
# Data types define the kind of value a variable can hold.
# Here are the main data types in Python:

# -------------------------
# 1. Numeric Data Types
# -------------------------

# Integers (int) - Whole numbers
num1 = 10
num2 = -5
print(type(num1))  # <class 'int'>

# Floating-Point Numbers (float) - Decimal numbers
pi = 3.14159
gravity = 9.8
print(type(pi))  # <class 'float'>

# Complex Numbers (complex) - Numbers with real and imaginary parts
complex_num = 2 + 3j
print(type(complex_num))  # <class 'complex'>

# -------------------------
# 2. Boolean Data Type
# -------------------------

# Booleans represent True or False values
is_python_fun = True
is_sky_green = False
print(type(is_python_fun))  # <class 'bool'>

# Booleans are actually integers underneath (True = 1, False = 0)
print(True + True)  # 2
print(False + True)  # 1

# -------------------------
# 3. String Data Type
# -------------------------

# Strings (str) are sequences of characters
greeting = "Hello, Python!"
name = 'Bright'
print(type(greeting))  # <class 'str'>

# Strings can be accessed using indexes
print(greeting[0])  # 'H'

# Multi-line strings use triple quotes
long_text = """This is
a multi-line
string."""
print(long_text)

# -------------------------
# 4. Sequence Data Types
# -------------------------

# Lists (list) - Ordered, mutable collections
numbers = [1, 2, 3, 4, 5]
mixed_list = [10, "Python", 3.14, True]
print(type(numbers))  # <class 'list'>

# Lists can be modified
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Tuples (tuple) - Ordered, immutable collections
coordinates = (10.0, 20.0)
person = ("Bright", 22, "Ghana")
print(type(coordinates))  # <class 'tuple'>

# Tuples cannot be changed (immutable)
# coordinates[0] = 15  # This will throw an error!

# Ranges (range) - Sequence of numbers
r = range(5)  # 0, 1, 2, 3, 4
print(list(r))

# -------------------------
# 5. Mapping Data Type
# -------------------------

# Dictionaries (dict) - Key-value pairs, unordered
person_info = {
    "name": "Bright",
    "age": 22,
    "country": "Ghana"
}
print(type(person_info))  # <class 'dict'>

# Accessing dictionary values
print(person_info["name"])  # 'Bright'

# -------------------------
# 6. Set Data Types
# -------------------------

# Sets (set) - Unordered collections of unique items
unique_numbers = {1, 2, 3, 4, 4, 5}
print(type(unique_numbers))  # <class 'set'>
print(unique_numbers)  # {1, 2, 3, 4, 5} (duplicates removed)

# Frozen Sets (frozenset) - Immutable sets
immutable_set = frozenset([1, 2, 3, 4])
# immutable_set.add(5)  # This will throw an error!

# -------------------------
# 7. None Type
# -------------------------

# None represents the absence of a value
nothing = None
print(type(nothing))  # <class 'NoneType'>

# -------------------------
# Dynamic Typing in Python
# -------------------------

# Python is dynamically typed, meaning variables can change types
x = 10  # int
x = "Now I'm a string"  # str
print(x)  # "Now I'm a string"

# -------------------------
# Type Conversion (Casting)
# -------------------------

# Convert between types
num_str = "100"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float
print(num_int, num_float)  # 100, 100.0

# -------------------------
# Conclusion
# -------------------------

# Python provides various built-in data types that allow you to store
# and manipulate different kinds of data efficiently.
# Understanding these types is key to writing better Python code.

