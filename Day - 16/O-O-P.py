# =========================
# Day 16: Object-Oriented Programming (OOP) in Python
# =========================

# ------------------------
# Introduction to OOP
# ------------------------

# Object-Oriented Programming (OOP) be a programming paradigm based on objects.
# Objects be instances of classes, which be blueprints for creating objects.

# Example of a simple class:
class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def bark(self):
        return "Woof! Woof!"

# Creating an object (instance of the Dog class)
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Woof! Woof!

# ------------------------
# Class Attributes & Instance Attributes
# ------------------------

# Class attributes be shared among all instances of a class.
# Instance attributes be specific to each object.

class Cat:
    species = "Mammal"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

cat1 = Cat("Whiskers")
print(cat1.name)  # Output: Whiskers
print(cat1.species)  # Output: Mammal

# ------------------------
# Methods in Classes
# ------------------------

# Methods be functions inside a class.
# They operate on the object's attributes.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.full_name())  # Output: Toyota Corolla