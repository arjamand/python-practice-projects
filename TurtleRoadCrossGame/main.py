import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score=Scoreboard()
# cars.add_cars()
# cars.add_cars()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

cars=[]
for c in range (200):
    carrr=CarManager()
    cars.append(carrr)
count=0
game_is_on = True
while game_is_on:
    # for c in cars.new_cars:
    #     c.forward(10)
    # print("hi")
    
    # count+=1
    # if count%5==0:
    #     cars[random.randint(0, 199)].forward(10)
    car.create_car()
    car.move()
    # for c in cars.new_cars:
    #     c.goto(c.xcor()-10, c.ycor())
        
    #     print("hii")
    # cars.move()
    # count=0
    # count+=1
    # if count%7==3:
    #     cars.add_cars()
        

    time.sleep(0.1)
    screen.update()
    
    if player.ycor() > 260:
        score.refresh_score()
        player.clear()
        player.setpos(0,-260)
        # player.left(90)
        car.move_increment+=5

    
    for c in car.new_cars:
        if c.distance(player)<20 :
            score.game_over()
            game_is_on=False
            # player.left(90)


screen.exitonclick()
