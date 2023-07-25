from turtle import *
import time
from snake import Snake
from snake import *
from food import Food
from scoreboard import Scoreboard

# from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# my_t.pensize(width=20)
# # my_t.shapesize(stretch_wid=10, stretch_len=10, outline=10)
# # my_t.hideturtle()
# my_t.back(40)

snake = Snake()
food = Food()
score = Scoreboard()
# snake.create_snake()

# snake.create_snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # for t in ts:
    #     t.forward(20)

    # ts[0].forward(20)
    snake.move()

    if snake.head.distance(food) < 15:

        food.refresh()
        score.refresh()
        snake.extend()
        # score.refresh()
        # score.refresh()
    # or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor > 280:
    if (
        snake.head.xcor() < -280
        or snake.head.xcor() > 280
        or snake.head.ycor() < -280
        or snake.head.ycor() > 280
    ):
        # game_on = False
        score.reset()
        snake.reset()
    for segments in snake.ts[1:]:

        # if segments == snake.head:
        #     pass
        if snake.head.distance(segments) < 10:
            # game_on = False
            score.reset()
screen.exitonclick()
