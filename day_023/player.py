from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()

        self.finish = FINISH_LINE_Y

        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.reset()

    def reset(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)
