# This code was coppied from my solution to the Reeborg's world Maze challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


# Robot can only turn left by default. Function to get him to turn right Hansel style.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Check that we aren't already at the goal    
while at_goal() == False:
    # If the path in front of you is clear, and a wall is on your right, move forward
    # This moves to keep the wall on the right side
    if front_is_clear() and wall_on_right():
        move()
    # If there isn't a wall on the right, and right is open, turn right and move
    elif right_is_clear() and not front_is_clear():
        turn_right()
        move()
    # This case will move you forward if you have no walls on any side.   
    elif front_is_clear():
        move()
    # If all else fails, turn left.
    else:
        turn_left()