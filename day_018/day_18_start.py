from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color('DarkGreen')

screen = Screen()
screen.colormode(255)

def square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)

def dashed():
    for i in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def overlap_shapes(start_sides=3, end_sides=10):
    for i in range(start_sides, end_sides):
        color = random_color()
        timmy.color(color)
        for x in range(i):
            timmy.forward(100)
            timmy.left(360/i)

def random_walk():
    timmy.pensize(5)
    timmy.speed("fast")
    angles = [0, 45, 90, 135, 180, 225, 270, 315]
    for _ in range(1000):
        color = random_color()
        timmy.color(color)

        timmy.forward(50)
        timmy.setheading(random.choice(angles))


def spirograph(num_of_circles = 10):
    heading = 0
    timmy.speed("fastest")
    for circle in range(1, num_of_circles + 1):
        color = random_color()
        timmy.color(color)

        timmy.setheading(heading)
        timmy.circle(300)
        heading += 360 / num_of_circles

spirograph(100)

screen.exitonclick()