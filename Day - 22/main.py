import time
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from charset_normalizer import detect

from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
# right paddle movement
screen.onkey(r_paddle.go_up,"Up")
# screen.onkeypress(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
# screen.onkeypress(r_paddle.go_down, "Down")
# left paddle movement
screen.onkey(l_paddle.go_up,"w")
# screen.onkeypress(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")
# screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect out of bounce on right side
    if ball.distance(r_paddle) > 50 and ball.xcor() > 320:
        ball.reset_position()
        scoreboard.l_point()

    # detect out of bounce on left side
    if ball.distance(l_paddle) > 50 and ball.xcor() < -320:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()