from turtle import Turtle, Screen
import pandas

# Constants for screen size and position
SCREEN_X = 800
SCREEN_Y = 600
START_POS_X = (1920 - SCREEN_X)/2
START_POS_Y = (1080 - SCREEN_Y)/2


screen = Screen()
screen.setup(width=SCREEN_X,height=SCREEN_Y, startx=START_POS_X,starty=START_POS_Y )
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

label = Turtle()
label.penup()
label.hideturtle()

# Pull all data from CSV into a DataFrame
state_data = pandas.read_csv("50_states.csv")

# Get List of states
states = state_data["state"].to_list()

# Initialize blank list of states
guessed_states = []
missing_states = []


# Main game loop
while len(guessed_states) < 50:

    # Prompt user for state, and make it Title Case
    answer_state = screen.textinput(f"{len(guessed_states)}/{len(states)} States Guessed", "Guess the name of a state:").title()

    #Check if state is in the list of states, and hasn't already been guessed
    if answer_state in states and answer_state not in guessed_states:
        # Add guessed state to list
        guessed_states.append(answer_state)
        # Extract the coordinates
        coordinates = state_data[state_data["state"] == answer_state]
        # Move labeler turtle instance to the coordinate on the state
        label.goto(int(coordinates.x), int(coordinates.y))
        label.write(answer_state, move=True, align="center", font=("Arial", 8, "normal"))
    elif answer_state.title() == "Exit":
        break

# Once out of the loop, make a list of the states that weren't guessed
for state in states:
    if state not in guessed_states:
        missing_states.append(state)

# Put those states in a dictionary
missing_state_dict = {
    "States": missing_states
}

# Make the dict a data frame to create the .csv
df = pandas.DataFrame(missing_state_dict)
df.to_csv("states_to_learn.csv")

screen.exitonclick()