from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        
        x_init = 0
        y_init = 0

        for _ in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.speed("fastest")
            segment.goto(x_init, y_init)
            x_init -= 20
            self.segments.append(segment)
        self.head = self.segments[0]
    
    def add_segment(self):
        segment = Turtle("square",visible=False)
        segment.color("white")
        segment.penup()
        segment.speed("fastest")
        segment.goto(self.segments[-1].position())
        segment.showturtle()
        self.segments.append(segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            leading_segment = self.segments[segment - 1]
            self.segments[segment].goto(leading_segment.position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    