# 2022-12-10 16:06:5fro

from turtle import *
from Padles import Padle
import ball
import time
from scoreboard import ScoreBoard

my_t = Turtle()
screen = Screen()
screen.setup(1000, 500)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

l_score = ScoreBoard()
l_score.l_score()
r_score = ScoreBoard()
r_score.r_score()

c_line = ScoreBoard()
c_line.centre_line()


r_padle = Padle()
r_padle.r_p_setup()
l_padle = Padle()
l_padle.l_p_setup()

ball = ball.Ball()

# screen.tracer(0)
screen.listen()
screen.onkey(r_padle.Up, "Up")
screen.onkey(r_padle.Down, "Down")
screen.onkey(l_padle.Up, "w")
screen.onkey(l_padle.Down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    if (
        ball.xcor() > 430
        and r_padle.distance(ball) < 50
        or ball.xcor() < -430
        and l_padle.distance(ball) < 50
    ):
        ball.bounce_x()

    if (
        ball.xcor() > 450
        and r_padle.distance(ball) > 50
        or ball.xcor() < -450
        and l_padle.distance(ball) > 50
    ):
        if ball.xcor() > 450 and r_padle.distance(ball) > 50:
            l_score.clear()
            l_score.l_score()
        elif ball.xcor() < -450 and l_padle.distance(ball) > 50:
            r_score.clear()
            r_score.r_score()

        ball.setpos(0, 0)
        ball.bounce_x()
        ball.bounce_y()


screen.exitonclick()
