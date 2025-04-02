from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.x_cord = cords[0]
        self.y_cord = cords[1]
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.x_cord,self.y_cord)

    def go_up(self):
        if self.ycor() < 240:
            nav_y =  self.ycor() + 20
            self.goto( self.xcor(), nav_y)

    def go_down(self):
        if  self.ycor() > -240:
            nav_y =  self.ycor() - 20
            self.goto( self.xcor(), nav_y)


