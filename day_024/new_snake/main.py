from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import random
import time

screen = Screen()
screen.setup(width=600, height=600, startx=660, starty=240)
screen.bgcolor("black")
screen.title("snek")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="w", fun = snake.up)
screen.onkey(key="s", fun = snake.down)
screen.onkey(key="a", fun = snake.left)
screen.onkey(key="d", fun = snake.right)

game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()
       
    if snake.head.distance(food) < 15:
        food.move()
        snake.add_segment()
        score.add_score()
    
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()

screen.exitonclick()