
from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(255, 255)
        self.pendown()
        for i in range(1, 5):
            self.right(90)
            self.forward(510)


        self.penup()