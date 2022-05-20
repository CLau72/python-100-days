from turtle import Turtle
import random
import time

BALL_DIRECTIONS = [-1, 1]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("normal")
        self.x_direction = 10
        self.y_direction = 10


    def ball_reset(self):
        self.home()
        self.x_direction *= random.choice(BALL_DIRECTIONS)
        self.y_direction *= random.choice(BALL_DIRECTIONS)
        time.sleep(1)

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_direction *= -1

    def paddle_bounce(self):
        self.x_direction *= -1