from turtle import Turtle, Screen
from paddles import Paddles
from scoreboard import Scoreboard, PitchLines
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(height=600, width=800)
scoreboard = Scoreboard()
lines = PitchLines()


paddle_1 = Paddles(-350)
paddle_2 = Paddles(350)
ball = Ball()

screen.listen()

screen.onkey(paddle_1.move_up, "w")
screen.onkey(paddle_1.move_down, "s")
screen.onkey(paddle_2.move_up, "Up")
screen.onkey(paddle_2.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(paddle_2) < 50 and ball.xcor() > 320 or ball.distance(paddle_1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        scoreboard.add_score1()
        ball.reset_position()
        

    if ball.xcor() < - 380:
        scoreboard.add_score2()
        ball.reset_position()


screen.exitonclick()
