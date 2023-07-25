# 2022-11-11 20:58:31

# #challange02

# from turtle import Turtle, Screen

# my_trtle = Turtle()

# # my_trtle.shape("arrow")
# for x in range(2, 103):
#     if x % 2 == 0:
#         my_trtle.penup()
#         my_trtle.forward(10)
#     else:
#         my_trtle.pendown()
#         my_trtle.forward(10)

#     if x == 40:
#         my_trtle.left(90)
#     if x == 60:
#         my_trtle.left(90)
# my_trtle.pendown()

# screen1 = Screen()
# screen1.exitonclick()


# # challange03
# from turtle import *
# from random import *
# my_trtle = Turtle()
# my_trtle.penup()
# my_trtle.setposition(0, 100)
# # print(my_trtle.pos())
# my_trtle.pendown()
# my_trtle.left(180)
# my_trtle.left(60)
# # colormode(255)
# # col = float(randint(0, 255))
# # # my_trtle.pencolor("brown")
# # for x in range(3, 11):
# #     my_trtle.pendown()
# #     if x == 3:
# #         angles = 180/x

# #     else:
# #         angles = 360/x

# #     my_trtle.left(angles)

# #     for y in range(x):

# #         my_trtle.forward(100)
# #         my_trtle.left(180)
# #         my_trtle.left(angles)
# #     my_trtle.right(angles)
# colors = ["yellow", " gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
#           "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

# # cc = colors[(randint(0, 20))]
# my_trtle.color(colors[(randint(0, 20))])
# for _ in range(3):

#     my_trtle.forward(100)
#     my_trtle.right(120)
#     if _ == 2:
#         my_trtle.left(30)
# my_trtle.color(colors[(randint(0, 20))])
# for __ in range(4):

#     my_trtle.forward(100)
#     my_trtle.right(90)
#     if __ == 3:
#         my_trtle.left(18)
# my_trtle.color(colors[(randint(0, 20))])
# for ___ in range(5):

#     my_trtle.forward(100)
#     my_trtle.right(72)
#     if ___ == 4:
#         my_trtle.left(12)
# my_trtle.color(colors[(randint(0, 20))])
# for ____ in range(6):

#     my_trtle.forward(100)
#     my_trtle.right(60)
#     if ____ == 5:
#         my_trtle.left(9)

# my_trtle.color(colors[(randint(0, 20))])
# for _____ in range(7):

#     my_trtle.forward(100)
#     my_trtle.right(51.4285714286)
#     if _____ == 6:
#         my_trtle.left(6.4285714286)

# my_trtle.color(colors[(randint(0, 20))])
# for ______ in range(8):

#     my_trtle.forward(100)
#     my_trtle.right(45)
#     if ______ == 7:
#         my_trtle.left(5)
# my_trtle.color(colors[(randint(0, 20))])
# for _______ in range(9):

#     my_trtle.forward(100)
#     my_trtle.right(40)
#     if _______ == 8:
#         my_trtle.left(4)
# my_trtle.color(colors[(randint(0, 20))])
# for ________ in range(10):

#     my_trtle.forward(100)
#     my_trtle.right(36)
#     if ________ == 9:
#         my_trtle.left(1)


# screen1 = Screen()
# screen1.exitonclick()


# # challange04

# from turtle import *
# import turtle
# from random import *
# my_turtle = Turtle()
# my_turtle.pensize(6)
# my_turtle, speed(0)
# turtle.colormode(255)


# def color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple


# # colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
# #           "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
# signal = False
# while signal == False:
#     # my_turtle.color(colors[(randint(0, 19))])
#     my_turtle.color(color())
#     rand = randint(1, 5)
#     if rand == 1:
#         my_turtle.forward(25)
#     elif rand == 2:
#         my_turtle.back(25)
#     elif rand == 3:
#         my_turtle.left(90)
#         my_turtle.forward(25)
#     elif rand == 4:
#         my_turtle.right(90)
#         my_turtle.forward(25)


# # def turn():
# #     my_turtle.back(25)


# # my_turtle.pensize(6)
# # my_turtle.forward(25)


# screen1 = Screen()
# screen1.exitonclick()


# challange 05


from turtle import *
import turtle
from random import *

turtle.colormode(255)


def color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


my_turtle = Turtle()
my_turtle.speed("fastest")
stop = 0
signal = True
while signal is True:
    my_turtle.color(color())
    my_turtle.circle(radius=100)
    my_turtle.left(6)
    stop += 1
    if stop == 60:
        signal = False


screen1 = Screen()
screen1.exitonclick()
