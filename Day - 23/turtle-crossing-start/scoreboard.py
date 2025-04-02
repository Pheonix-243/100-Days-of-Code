from  turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.setup_scoreboard()

    def setup_scoreboard(self):
        self.color("black")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        # Clear and rewrite the level
        self.clear()
        self.increase_level()
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def increase_level(self):
        # Increment level and update display
        self.level += 1

    def game_over(self):
        # Display "GAME OVER" at center
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\n Level: {self.level}", align="center", font=FONT)