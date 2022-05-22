import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen size and position constants
SCREEN_X = 600
SCREEN_Y = 600
START_POS_X = (1920 - SCREEN_X)/2
START_POS_Y = (1080 - SCREEN_Y)/2

screen = Screen()
screen.setup(width=SCREEN_X, height=SCREEN_Y, startx=START_POS_X, starty=START_POS_Y)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.up)

loop_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Move all cars and check for collision with player
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()
        
        # remove cars that go offscreen
        if car.xcor() <= -350:
            car_manager.all_cars.remove(car)

    if player.ycor() >= player.finish:
        player.reset()
        level = scoreboard.level_up()
        print(level)
        car_manager.speed_up()


    if loop_count >= 6:
        car_manager.new_car()
        loop_count = 0
    
    loop_count += 1

screen.exitonclick()