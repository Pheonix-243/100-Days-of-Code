import turtle as t
from turtle import Turtle, Screen

import random

tim = Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for  _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))









screen = t.Screen()
screen.exitonclick()