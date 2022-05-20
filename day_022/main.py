from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Constants for screen size and position
SCREEN_X = 800
SCREEN_Y = 600
START_POS_X = (1920 - SCREEN_X)/2
START_POS_Y = (1080 - SCREEN_Y)/2

# Constants for player paddles and scoreboard. Calculated based on screen size
PLAYER1_START = (-(SCREEN_X/2 - 50),0)
PLAYER2_START = ((SCREEN_X/2 - 50),0)
PLAYER1_SCOREBOARD = (-(SCREEN_X/4),((SCREEN_Y/2)- 100))
PLAYER2_SCOREBOARD = ((SCREEN_X/4),((SCREEN_Y/2)- 100))

screen = Screen()
screen.setup(width=SCREEN_X, height=SCREEN_Y, startx=660, starty=240)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle(PLAYER1_START, SCREEN_Y)
p1_score = Score(PLAYER1_SCOREBOARD)
player2 = Paddle(PLAYER2_START, SCREEN_Y)
p2_score = Score(PLAYER2_SCOREBOARD)
ball = Ball()

screen.listen()
screen.onkey(key="w",fun=player1.up)
screen.onkey(key="Up",fun=player2.up)
screen.onkey(key="s",fun=player1.down)
screen.onkey(key="Down",fun=player2.down)


ball.ball_reset()
game_active = True
while game_active:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if abs(ball.ycor()) >= (SCREEN_Y/2 - 20):
        ball.wall_bounce()

    if ball.xcor() == (player1.xcor() + 10) and ball.distance(player1) <= 60:
        ball.paddle_bounce()

    if ball.xcor() == (player2.xcor() - 10) and ball.distance(player2) <= 60:
        ball.paddle_bounce()

    if ball.xcor() > (SCREEN_X/2 + 20):
        p1_score.point_scored()
        ball.ball_reset()

    if ball.xcor() < (-SCREEN_X/2 - 20):
        p2_score.point_scored()
        ball.ball_reset()

    if p1_score.score >= 7 or p1_score.score >=7:
        p1_score.game_over()
        game_active = False

screen.exitonclick()