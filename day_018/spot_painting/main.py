import colorgram
import random
from turtle import Turtle, Screen


painter = Turtle()
painter.shape("turtle")
painter.speed("fastest")
painter.penup()

screen = Screen()
screen.colormode(255)

def color_pallet(image_file, num_colors):
    pallet = colorgram.extract(image_file, num_colors)
    rgb_pallet = []

    for color in (pallet):
        rgb_color = color.rgb
        rgb_pallet.append(rgb_color)

    return rgb_pallet
    

def painting(x_dots, y_dots, pallet_source, pallet_depth):
    # Generate color pallet list
    colors = color_pallet(pallet_source, pallet_depth)

    for y in range(y_dots):
        if y % 2 == 0 or y == 0:
            painter.setheading(0)
        else:
            painter.setheading(180)
        for x in range(x_dots):
            painter.dot(20,random.choice(colors))
            if x < x_dots - 1:
                painter.forward(50)
        painter.setheading(90)
        painter.forward(50)
        


painting(10,10,"./art/atl.jpg",7)

screen.exitonclick()