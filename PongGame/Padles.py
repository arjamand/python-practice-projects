from turtle import Turtle


class Padle(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        # self.goto(450, 0)
        self.speed("fastest")
        self.left(90)
        self.Up()
        self.Down()

    def r_p_setup(self):
        self.setpos(450, 0)

        self.showturtle()

    def l_p_setup(self):
        self.setpos(-450, 0)

        self.showturtle()

    def Up(self):
        self.forward(30)

    def Down(self):
        self.back(30)
