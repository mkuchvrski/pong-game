from turtle import Turtle


class Paddles(Turtle):

    def __init__(self, x_coordinate):
        super().__init__()
        self.goto(x_coordinate, 0)
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move_up(self):
        self.sety(self.ycor()+20)

    def move_down(self):
        self.sety(self.ycor()-20)
    