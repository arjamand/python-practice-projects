from turtle import Turtle
# from scoreboard import Scoreboard
import random
# from scoreboard import *

# score = Scoreboard()


class Food(Turtle):
    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        x_size = random.randint(-280, 280)
        y_size = random.randint(-280, 280)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(x_size, y_size)
        # self.refresh()
        # score = Scoreboard()

    def refresh(self):
        # self.score.clear()
        # Scoreboard.refresh()
        # score.refresh()
        x_size = random.randint(-280, 280)
        y_size = random.randint(-280, 280)
        self.goto(x_size, y_size)

    # def hit_edge(self):
    #     score.game_over()
