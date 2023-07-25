from turtle import *


STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.ts_count = 2
        self.ts = []
        self.create_snake()
        self.head = self.ts[0]
        # self.move()

    def create_snake(self,):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        my_t = Turtle()
        my_t.shape("square")
        my_t.color("white")
        my_t.penup()
        my_t.goto(position)
        self.ts.append(my_t)

    def extend(self):
        self.ts_count += 1
        self.add_segment(self.ts[-1].position())

    def move(self):
        for t_num in range(self.ts_count, 0, -1):
            new_x = self.ts[t_num-1].xcor()
            new_y = self.ts[t_num-1].ycor()
            self.ts[t_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.ts:
            seg.goto(1000,1000)
        self.ts_count = 2
        self.ts.clear()
        self.create_snake()
        self.head=self.ts[0]
        
        
        