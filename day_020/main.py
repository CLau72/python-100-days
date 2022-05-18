from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600, startx=660, starty=240)
screen.bgcolor("black")
screen.title("snek")

snake_segments = []

x_position = 10
y_position = 0

for snake_segment in range(3):
    snake = Turtle("square")
    snake.color("white")
    snake.speed("fastest")
    snake.penup()
    snake.goto(x_position,y_position)
    x_position -= 20
    snake_segments.append(snake)
    

def up():
    snake.setheading(90)

def down():
    snake.setheading(270)

def left():
    snake.setheading(180)

def right():
    snake.setheading(0)

while True:
    for segment in snake_segments:
        segment.forward(20)
       
    time.sleep(1)

    screen.listen()
    screen.onkey(key="w", fun = up)
    screen.onkey(key="s", fun = down)
    screen.onkey(key="a", fun = left)
    screen.onkey(key="d", fun = right)

screen.exitonclick()