# This is a sample Python script.
import turtle
from turtle import *
import random

timmy = Turtle()
#timmy.shape("turtle")
# timmy.color("grey")
turtle.colormode(255)
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# for i in range(1,5):
#     timmy.forward(100)
#     timmy.right(90)

# for i in range(1,50):
#     timmy.forward(5)
#     timmy.pu()
#     timmy.forward(5)
#     timmy.pd()
#
# for i in range(3,11):
#     timmy.color(random.choice(colours))
#     angle = (i-2)*180/i
#     for j in range(0,i):
#         timmy.forward(100)
#         timmy.right(180-angle)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return  random_color

timmy.pensize(1)
#directions = [0, 90, 180, 270]
timmy.speed("fastest")
# for i in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

for i in range(5, 365, 5):
    timmy.color(random_color())
    timmy.circle(80)
    timmy.setheading(i)




screen = Screen()
screen.exitonclick()