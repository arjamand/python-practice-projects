from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setpos(0, -280)
        self.left(90)

    def move_up(self):
        if self.ycor() < 280:
            # self.goto(0, self.ycor()+MOVE_DISTANCE)
            self.forward(MOVE_DISTANCE)
        # elif self.ycor() >= 280:
        #     print("You Win")

    def move_down(self):
        if self.ycor() < 280 and self.ycor() > -270:
            #self.goto(0, self.ycor()-MOVE_DISTANCE)
            self.back(MOVE_DISTANCE)
        elif self.ycor() >= 280:
            print("You Win")

