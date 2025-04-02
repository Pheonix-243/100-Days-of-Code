import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()


# Set up keyboard binding for player movement
screen.listen()
screen.onkey(player.move_up,"Up")

scoreboard.setup_scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            print("You collided a with car")
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.update_scoreboard()



screen.exitonclick()
