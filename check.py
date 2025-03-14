import os  # Unused import

def my_function():  # Missing docstring
    x = 140  # Poor variable naming
    y = 240  # Unused variable
    print(x)

class MyClass:  # Missing docstring
    def __init__(self):
        self.a = 1  # Poor variable naming

    def method_one(self):  # Missing docstring
        b = 452  # Poor variable naming
        print(b)

def another_function():  # Missing docstring
    for i in range(10):
        print(i)
        if i==5:  # Inconsistent spacing around operator
            print("Found 5")