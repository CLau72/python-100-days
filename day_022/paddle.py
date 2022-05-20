from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,start_position,screen_height):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5.0,stretch_len=1.0)
        self.goto(start_position)
        self.movement_range = screen_height

    def up(self):
        if (self.ycor()+ 50) < self.movement_range/2:
            self.sety(self.ycor() + 20)

    def down(self):
        if (self.ycor()- 50) > -self.movement_range/2:    
            self.sety(self.ycor() - 20)