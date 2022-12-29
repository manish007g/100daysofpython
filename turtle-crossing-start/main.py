import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SLEEP_TIME = 0.3
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    car.car_move()
    screen.update()

    car.create_car()
    car.car_move()

    #Detect Collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #player reached the final line
    if player.ycor() > 280:
        scoreboard.inc_score()
        player.goto(0, -280)
        SLEEP_TIME -= 0.03

screen.exitonclick()
