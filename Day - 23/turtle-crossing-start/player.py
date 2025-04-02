from  turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()


    def create_player(self):
        # Create turtle, set shape, color, starting position
        self.color("black")
        self.left(90)
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.go_to_start()


    def move_up(self):
        # Move the player forward by MOVE_DISTANCE
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        # Return True if player reached the top
        if self.ycor() == 270:
            return True
        else:
            return False

    def go_to_start(self):
        # Return player to starting position
        self.goto(STARTING_POSITION)