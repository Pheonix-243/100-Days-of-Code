# An Object is an instance fo a class which is made of methods and attributes
# Attributes are variables and methods are functions
# A class can have multiple objects
#
# import turtle
#
# from turtle import Turtle, Screen
#
# lee = Turtle()
#
# screen = Screen()
# lee.speed(5)
# lee.shape("square")
# lee.color("coral")
# lee.forward(54)
#
# print(lee)
#
# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name", ["Ama", "John", "Candy"],)
table.add_column("School", ["Knust", "UCC", "Umat"],)

table._align = 

print(table)