from turtle import Turtle
import time
import random


class Ball(Turtle):
    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.setposition(0, 0)
        self.penup()
        self.xmove = 15
        self.ymove = 10

        # self.x_cord = [-20, 20]
        # self.y_cord = [-15, 15]

        # if self.x_cor == 0 and self.y_cor == 0:
        #     self.x_cor = random.choice(self.x_cord)
        #     self.y_cor = random.choice(self.y_cord)

    def move(self):
        self.x_cor = self.xcor()+self.xmove
        self.y_cor = self.ycor()+self.ymove
        self.goto(self.x_cor, self.y_cor)

        self.speed("normal")

        # while self.xcor() < 450:
        # while True:
        #     if self.ycor() == 240 and self.xcor() < 0:
        #         # while self.xcor() < 480:
        #         while self.xcor() < 480 or self.xcor() > -480:
        #             self.y_cor -= 15
        #             self.x_cor -= 20
        #             self.goto(self.x_cor, self.y_cor)
        #             time.sleep(.1)

        #     if self.ycor() == 240 and self.xcor() > 0:
        #         while self.xcor() < 480 or self.xcor() > -480:
        #             self.y_cor -= 15
        #             self.x_cor += 20
        #             self.goto(self.x_cor, self.y_cor)
        #             time.sleep(.1)

        #     if self.ycor() == -240 and self.xcor() < 0:
        #         while self.xcor() < 480 or self.xcor() > -480:
        #             self.goto(self.x_cor, self.y_cor)
        #             self.x_cor -= 20
        #             self.y_cor += 15
        #             time.sleep(.1)

        #     if self.ycor() == -240 and self.xcor() > 0:
        #         while self.xcor() < 480 or self.xcor() > -480:
        #             self.goto(self.x_cor, self.y_cor)
        #             self.x_cor += 20
        #             self.y_cor += 15
        #             time.sleep(.1)

        # if self.xcor() < 480 and self.xcor() > -480:
        #     if self.x_cor > 0:
        #         self.x_cor += 20
        #     elif self.x_cor < 0:
        #         self.x_cor -= 20
        #     if self.y_cor > 0:
        #         self.y_cor += 15
        #     elif self.y_cor < 0:
        #         self.y_cor -= 15
        #     self.goto(self.x_cor, self.y_cor)
        #     time.sleep(.1)
        # #         # self.y_cor += 15
        # #         # self.goto(self.x_cor, self.y_cor)
    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
