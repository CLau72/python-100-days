from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = -1
        self.penup()
        self.pencolor("white")
        self.update_score()
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        self.home()
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)
        