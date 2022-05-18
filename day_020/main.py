from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600, startx=660, starty=240)
screen.bgcolor("black")
screen.title("snek")
screen.tracer()

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
    
snake_head = snake_segments[0]

def up():
    snake_head.setheading(90)

def down():
    snake_head.setheading(270)

def left():
    snake_head.setheading(180)

def right():
    snake_head.setheading(0)

while True:
    screen.update()
    time.sleep(0.2)
    for segment in range(len(snake_segments) - 1,0,-1):
        leading_segment = snake_segments[segment-1]
        snake_segments[segment].goto(leading_segment.position())
       
    screen.listen()
    screen.onkey(key="w", fun = up)
    screen.onkey(key="s", fun = down)
    screen.onkey(key="a", fun = left)
    screen.onkey(key="d", fun = right)

    snake_segments[0].forward(20)

screen.exitonclick()