from turtle import Turtle
ALIGN = "center"
FONTS = ("Arial", 25, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()
 
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 210)
        self.write(f"SCORE:\n{self.score1}          {self.score2}", align=ALIGN, font=FONTS)


    def add_score1(self):
        self.score1 += 1
        self.update_scoreboard()
    
    def add_score2(self):
        self.score2 += 1
        self.update_scoreboard()
    
    def game_over(self,user):
        self.goto(0,0)
        self.write(f"GAME OVER!\n{user} WON\n SCORE:\n{self.score1}          {self.score2}", align=ALIGN, font=FONTS)
    

class PitchLines(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.width(5)
        self.goto(0, 300)
        self.setheading(270)
        self.draw_line()
    
    def draw_line(self):
        for n in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
    

    

