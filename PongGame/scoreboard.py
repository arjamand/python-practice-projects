from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.l_arg = -1
        self.r_arg = -1

    def l_score(self):

        self.l_arg += 1
        self.goto(-100, 200)
        self.pendown()
        self.write(f"{self.l_arg}", font=("Arial", 32, "normal"))
        self.penup()

    def r_score(self):

        self.r_arg += 1
        self.goto(100, 200)
        self.pendown()
        self.write(f"{self.r_arg}", font=("Arial", 32, "normal"))
        self.penup()

    def centre_line(self):
        self.penup()
        self.goto(0, -250)
        self.left(90)

        while self.ycor() < 250:
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(20)

    # l_score
