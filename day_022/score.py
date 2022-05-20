from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Lucida Console", 60, "bold")

class Score(Turtle):

    def __init__(self,score_position):
        super().__init__()
        self.score = 0
        self.position = score_position
        
        self.hideturtle()
        self.color("white")
        self.penup()
        
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(self.position)
        self.write(f"{self.score}", True, align=ALIGNMENT,font=FONT)

    def point_scored(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", True, align=ALIGNMENT,font=FONT)