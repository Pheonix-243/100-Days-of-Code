from turtle import Screen , Turtle
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


game = Snake()
food = Food()

score = ScoreBoard()

screen.listen()
screen.onkey(game.up,"Up")
screen.onkey(game.down,"Down")
screen.onkey(game.left,"Left")
screen.onkey(game.right,"Right")

score.show_score()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    game.move_snake()

    if game.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        game.extend()


    # detect collision with wall
    if game.head.xcor() > 280 or game.head.xcor() < -300 or game.head.ycor() > 280 or game.head.ycor() < -280:
        score.reset()
        game.reset()

    # detect collision with tail
    for segment in game.segments[1:]:
        if game.head.distance(segment) < 10:
            score.reset()
            game.reset()




screen.exitonclick()