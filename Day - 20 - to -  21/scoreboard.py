from turtle import Turtle


ALIGNMENT = "center"
FONT= ("courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        with open("high_scores.txt") as file:
            self.high_score = file.read()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,250)
        self.show_score()

    def increase_score(self):
        self.player_score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.player_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        if self.player_score > int(self.high_score):
            self.high_score = self.player_score
        with open("high_scores.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.player_score = 0
        self.show_score()

    #     self.write(f" Game Over\nYou scored: {self.player_score}",align=ALIGNMENT, font=FONT)
    # def game_over(self):
    #     self.goto(0,0)
    #     self.clear()
    #     self.write(f" Game Over\nYou scored: {self.player_score}",align=ALIGNMENT, font=FONT)
