# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)


# from turtle import *
# import turtle
# from random import randint
# my_turtle = Turtle()

# turtle.colormode(255)


# def color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple


# colors = [(251, 167, 43), (183, 76, 183), (159, 92, 119), (231, 208, 235), (229, 100, 190), (36, 41, 155), (6, 151, 157), (185, 50, 243), (73, 35, 189), (128, 63, 241), (49, 236, 137), (248, 233, 234), (52, 18, 246), (28, 134, 36), (252, 210, 207), (220, 134, 252), (122, 130, 0), (23, 165, 19), (18, 236, 212), (85, 94, 143), (191, 59, 27), (115, 16, 136), (86, 252, 182), (202, 189, 41), (7, 137, 214), (54, 168,
# 121), (127, 200, 252), (140, 74, 35), (142, 112, 27), (120, 220, 249)]
# for c in range(30):
#     colors.append(color())

# print(colors)

import random
from random import choice
import turtle
from turtle import *
turtle.colormode(255)

my_turtle = Turtle()
my_turtle.hideturtle()

my_turtle.penup()
my_turtle.setposition(-250, -200)
my_turtle.pendown()

my_turtle.speed("fastest")

colors = [(251, 167, 43), (183, 76, 183), (159, 92, 119), (231, 208, 235), (229, 100, 190), (36, 41, 155), (6, 151, 157), (185, 50, 243), (73, 35, 189), (128, 63, 241), (49, 236, 137), (248, 233, 234), (52, 18, 246), (28, 134, 36), (252, 210, 207), (220, 134, 252), (122, 130, 0), (23, 165, 19), (18, 236, 212), (85, 94, 143), (191, 59, 27), (115, 16, 136), (86, 252, 182), (202, 189, 41), (7, 137, 214), (54, 168,
                                                                                                                                                                                                                                                                                                                                                                                                                      121), (127, 200, 252), (140, 74, 35), (142, 112, 27), (120, 220, 249)]


def color():
    # col = 0
    # r = colors[col][0]
    # g = colors[col][1]
    # b = colors[col][2]
    my_tuple = random.choice(colors)
    # col += 1
    return my_tuple


def reset():
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.left(180)


count = 0
count2 = 0
while True:
    my_turtle.pendown()
    my_turtle.color(color())
    my_turtle.dot(20)
    my_turtle.penup()
    my_turtle.forward(50)
    count += 1

    if count == 10:
        count = 0
        count2 += 1
        reset()
    if count2 == 10:
        break


t_screen = Screen()
t_screen.exitonclick()
