from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400, startx=720, starty=340)

colors = ["purple", "blue", "green", "yellow", "orange", "red"]

def turtle_gen(color):
    turtle_color = color
    color = Turtle(shape='turtle')
    color.color(turtle_color)
    color.penup()
    return color


bet = screen.textinput('Place Your Bet!', "Select the turtle you think will win. \nPurple\nBlue\nGreen\nYellow\nOrange\nRed").lower()

x_start = -230
y_start = 125

for color in colors:
    turtle_color = color
    color = turtle_gen(turtle_color)
    color.goto(x_start,y_start)
    y_start -= 50





screen.exitonclick()
