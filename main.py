import random
import turtle
from random import choice, randint

# for taking most common colors from image
# import colorgram
# color = [(i.rgb.r, i.rgb.g, i.rgb.b) for i in colorgram.extract('image.jpg', 10)]

colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216)]


def spot_with_color(radius):
    my_turtle.dot(radius, random.choice(colors))


def one_line(spot_cnt):
    for _ in range(spot_cnt):
        spot_with_color(20)
        my_turtle.forward(50)


def go_to_next_line(line):
    my_turtle.penup()
    my_turtle.goto(-250, -200 + (line * 50))


def draw_spot_picture(size, spots):
    for i in range(size):
        go_to_next_line(i)
        one_line(spots)


my_turtle = turtle.Turtle()
my_turtle.speed('fastest')
my_turtle.hideturtle()
turtle.colormode(255)

draw_spot_picture(10, 10)

screen = turtle.Screen()
screen.screensize(500, 500)
screen.exitonclick()
