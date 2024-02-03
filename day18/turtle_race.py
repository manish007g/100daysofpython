import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
y_position = [-60, -40, -20, 0, 20, 40]
all_turtles=[]
timmy = Turtle()
timmy1 = Turtle()
timmy1.pu()
timmy.pu()
timmy.goto(x=200,y=200)
timmy1.goto(x=-240, y=200)
timmy.pd()
timmy1.pd()
timmy.goto(x=200, y=-200)
timmy1.goto(x=-240, y=-200)


for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.pu()
    tim.goto(x=-230, y=y_position[i])
    all_turtles.append(tim)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race!! Enter the color : ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtl in all_turtles:
        if turtl.xcor() > 200:
            is_race_on = False
            winning_color=turtl.pencolor()
            if winning_color==user_bet:
                print (f"You have won!! The {winning_color} is the winner")
                break
            else:
                print(f"You have Lost!! The {winning_color} is the winner")
                break
        turtl.forward(random.randint(0, 10))

screen = Screen()
screen.setup(width=500, height=400)




screen.exitonclick()