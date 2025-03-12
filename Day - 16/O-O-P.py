# An Object is an instance fo a class which is made of methods and attributes
# Attributes are variables and methods are functions
# A class can have multiple objects

import turtle

from turtle import Turtle, Screen

lee = Turtle()

screen = Screen()
lee.speed(5)
lee.shape("square")
lee.color("coral")
lee.forward(54)

print(lee)

screen.exitonclick()