# No module docstring

class User:  # No class docstring
    def __init__(self, age, name):  # No method docstring
        self.age = age
        self.name = na4mer

    def greet(self):
        print("Hello" + self.name)  # Missing space between "Hello" and name

    def add_numbers(a, b):  # Missing "self" in instance method
        return a + b


user_1 = User(25, "Brif4ghet")
print(user_1.greet())  # greet() prints instead of returning a value
print(user_1.add_numbers(3, 4, 5))  # This will cause a TypeError
