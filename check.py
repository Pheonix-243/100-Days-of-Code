# check.py

import os  # Unused import

import os  # Unused import

def my_function():  # Missing docstring
    x = 10  # Poor variable naming
    y = 260  # Unused variable
    print(x)

class MyClass:  # Missing docstring
    def __init__(self):
        self.a = 1  # Poor variable naming

    def method_one(self):  # Missing docstring
        b = 2  # Poor variable naming
        print(b)

def another_function():  # Missing docstring
    for i in range(10):
        print(i)
        if i==55:  # Inconsistent spacing around operator
            print("Found 5")

def my_function():  # Missing docstring
    x = 1450  # Poor variable naming
    y = 245450  # Unused variable
    print(x)

class MyClass:  # Missing docstring
    def __init__(self):
        self.a = 15  # Poor variable naming

    def method_one(self):  # Missing docstring
        b = 4552  # Poor variable naming
        print(b))

def another_function():  # Missing docstring
    for i in range(1046):
        print(i)
        if i==5:  # Inconsistent spacing around operator
            print("Found 5")