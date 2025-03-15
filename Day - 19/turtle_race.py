
import random
from turtle import Turtle,Screen

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
y_positions = [-70, -40, -10, 20,50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        random_turtle = random.choice(all_turtles)
        random_turtle.forward(random_distance)
        if random_turtle.xcor() > 230:
            is_race_on = False
            if random_turtle.pencolor() == user_bet:
                print(f"You won!🤩 Turtle with color {random_turtle.pencolor()} won the race")
            else:
                print(f"You lost the bet😶 Turtle with color {random_turtle.pencolor()} won the race")





screen.exitonclick()