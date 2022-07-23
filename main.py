import colorgram
import turtle
from turtle import Turtle, Screen
import random

color_data = colorgram.extract('dots.jpeg', 400)
colors = []


for entry in range(len(color_data)):
    color = (color_data[entry].rgb.r, color_data[entry].rgb.g, color_data[entry].rgb.b)
    colors.append(color)

color_list = [(193, 159, 121), (146, 163, 183), (70, 99, 126), (136, 91, 68), (188, 149, 166), (221, 205, 130), (23, 39, 54), (132, 77, 96), (146, 172, 157), (73, 111, 89), (163, 149, 68), (18, 47, 38), (215, 176, 190), (55, 40, 29), (173, 99, 122), (183, 101, 85), (181, 187, 210), (109, 123, 157), (222, 178, 170), (43, 59, 97), (51, 31, 40), (98, 147, 118), (104, 44, 58), (174, 203, 190), (27, 86, 65), (108, 47, 41), (166, 202, 210), (82, 144, 158), (27, 80, 89), (74, 72, 41), (221, 201, 29)]

timmy = Turtle()
turtle.colormode(255)
timmy.penup()

def one_line_of_dots():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.fd(50)

def ten_rows():
    y = 0
    for _ in range(10):
        one_line_of_dots()
        y += 50
        timmy.setx(0)
        timmy.sety(y)

ten_rows()

screen = Screen()
screen.exitonclick()