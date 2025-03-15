from turtle import Turtle, Screen

timo = Turtle()
screen= Screen()

def move_forward():
    timo.forward(10)

def move_backward():
    timo.backward(10)

def turn_left():
    current_heading = timo.heading()
    timo.setheading(current_heading - 10)

def turn_right():
    current_heading = timo.heading()
    timo.setheading(current_heading + 10)

def clear():
    timo.clear()
    timo.penup()
    timo.home()
    timo.pendown()


screen.listen()

# A higher order function is a function that can work with other functions by accepting them as arguments
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()