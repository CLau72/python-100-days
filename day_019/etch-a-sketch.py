from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()



def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)
def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def reset():
    turtle.clear()
    turtle.reset()


screen.listen()

screen.onkey(key="w", fun = move_forward)
screen.onkey(key="s", fun = move_backward)
screen.onkey(key="a", fun = turn_left)
screen.onkey(key="d", fun = turn_right)
screen.onkey(key="c", fun = reset)



screen.exitonclick()