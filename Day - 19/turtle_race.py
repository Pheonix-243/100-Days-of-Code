import random
from turtle import Turtle, Screen

IS_RACE_ON = False

SCREEN = Screen()
SCREEN.setup(width=500, height=400)
user_bet = SCREEN.textinput(
    title="Make your bet now",
    prompt="Which turtle will win the race? Enter a color:"
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create turtles
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    IS_RACE_ON = True

while IS_RACE_ON:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            IS_RACE_ON = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won the bet! 🤩 The {winning_color} turtle won the race!")
            else:
                print(f"You lost the bet! 😶 The {winning_color} turtle won the race.")

SCREEN.exitonclick()
