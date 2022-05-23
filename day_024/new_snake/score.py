from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        with open("./high_score.txt") as f:
            self.high_score = int(f.read())
        self.penup()
        self.pencolor("white")
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} - High Score: {self.high_score}", True, align=ALIGNMENT,font=FONT)
    
    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./high_score.txt","w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

        