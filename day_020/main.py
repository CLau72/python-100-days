from turtle import Turtle, Screen
from snake import Snake
import random
import time

screen = Screen()
screen.setup(width=600, height=600, startx=660, starty=240)
screen.bgcolor("black")
screen.title("snek")
screen.tracer()

snake = Snake()

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
       
    screen.listen()
    screen.onkey(key="w", fun = snake.up)
    screen.onkey(key="s", fun = snake.down)
    screen.onkey(key="a", fun = snake.left)
    screen.onkey(key="d", fun = snake.right)
    screen.onkey(key="space", fun = snake.add_segment)


screen.exitonclick()