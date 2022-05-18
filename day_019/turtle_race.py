from turtle import Turtle, Screen, turtles
import random

screen = Screen()
screen.setup(width=500, height=400, startx=720, starty=340)

# Create lists for the colors of the turtles, and an empty list the turtles will be placed in later
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
all_turtles = []

# Function that returns a turtle object with a given color
def turtle_gen(color):
    turtle_color = color
    color = Turtle(shape='turtle')
    color.color(turtle_color)
    color.penup()
    return color

# Prompt user to place a bet on one of the turtles
bet = screen.textinput('Place Your Bet!', "Select the turtle you think will win. \nPurple\nBlue\nGreen\nYellow\nOrange\nRed").lower()

# Used for initilizing starting line coordinates
x_start = -230
y_start = 125

# For every color, make a turtle of that color, place it to the starting line, and add it to the all_turtles list
for color in colors:
    turtle_color = color
    color = turtle_gen(turtle_color)
    color.goto(x_start,y_start)
    all_turtles.append(color)
    y_start -= 50

# Set race state to active, and initialize the winner string
race_active = True
winner = ""

# Main race loop
while race_active:


    # For each turtle in the list, check if the race is active, and move the turtle a random distance.
    # If the turtle passes the finish line, set the race state to false and set the winner.
    for turtle in all_turtles:
        if race_active:
            turtle.forward(random.randint(0,10))
            distance_traveled = turtle.position()
        if distance_traveled[0] >= 230 and race_active:
            winner = turtle.fillcolor()
            race_active = False

# If the bet string equals the winning turtle string, print the win state, otherwise tell the player they lost.            
if winner == bet:
    print(f"You win! {winner.title()} won the race!")
else:
    print(f"You lose. {bet.title()} did not win. {winner.title()} was the winner.")

# Used to close screen
screen.exitonclick()
