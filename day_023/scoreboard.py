from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        
        self.hideturtle()
        self.color("black")
        self.penup()
        
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-160, 260)
        self.write(f"Level: {self.level + 1}", True, align="center",font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score()
        return self.level

    def game_over(self):
        self.home()
        self.write("GAME OVER", True, align="center",font=FONT)
