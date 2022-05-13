#!/usr/bin/env python3

from turtle import Turtle, Screen
import time

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkSeaGreen4")


my_screen = Screen()
my_screen.screensize(canvwidth=240,canvheight=240)
print(my_screen.canvheight)
print(my_screen.canvwidth)


time.sleep(5)
timmy.forward(100)

my_screen.exitonclick()