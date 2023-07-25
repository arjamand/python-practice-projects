from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

starting_pos = (340, random.randint(-260, 260))


class CarManager():
    def __init__(self):
        self.move_increment = 10
        self.new_cars = []
        
        
    def create_car(self):
        r_num=random.randint(0, 6)
        if r_num==4:
            
            n_car=Turtle()
            n_car.penup()
            n_car.shape("square")
            n_car.setpos(340,random.randint(-260, 260))

            n_car.color(random.choice(COLORS))
            n_car.shapesize(1, 2)
            n_car.left(180)
            self.new_cars.append(n_car)
        
  
    def move(self):
        for c in self.new_cars:
            c.forward(self.move_increment
        )
            
        
        # self.goto(self.xcor()-self.move_increment
        #, self.ycor())

        # self.forward(20)

        # my_c = self.new_cars[random.randint(0, 49)]
        # my_c.forward(self.move_increment
        #)
        # print(my_c)
        # my_c.goto(my_c.xcor()-self.move_increment
        #, my_c.ycor())
        # print(self.new_cars)
        # for nc in self.new_cars:
        #     # nc.goto(self.xcor()-self.move_increment
        #, self.ycor())
        #     # time.sleep(0.01)
        #     while nc.xcor() < -300:
        #         nc.goto(nc.xcor()-self.move_increment
        #, nc.ycor())

    # def create_cars(self):
    #     pass

    # def create_cars(self,):
    #     for position in starting_pos:

    #         self.add_segment(position)

    # def add_cars(self):           
    #         my_c = Turtle()
    #         my_c.shape("square")
    #         my_c.penup()
    #         my_c.setpos(260, random.randint(-260, 260))

    #         my_c.color(random.choice(COLORS))
    #         my_c.shapesize(1, 2)
    #         my_c.left(180)
    #         self.new_cars.append(my_c)
