from turtle import Turtle


import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_wid=1.0, stretch_len=2.0)
        car.goto(350,random.randint(-250,250))
        car.color(random.choice(COLORS))
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)
    
    def speed_up(self):
        self.speed += MOVE_INCREMENT



