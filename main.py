<<<<<<< HEAD
from turtle import Turtle, Screen
=======
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# making the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Mania")
screen.tracer(0)

# making the paddle
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# making a Ball
ball = Ball()

# making a scoreboard
score = ScoreBoard()

screen.listen()

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.mov_speed)
    screen.update()
    ball.move()

    # Detecting the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detecting the collision with the Paddle

    if ball.distance(l_paddle) < 40 and ball.xcor() < -320 or ball.distance(r_paddle) < 40 and ball.xcor() > 320:
        ball.bounce_paddle()

    # Detect right paddle miss of ball
    if ball.xcor() > 380:
        ball.reset()
        score.score_l()

    # Detect the Left paddle miss of ball
    if ball.xcor() < -380:
        ball.reset()
        score.score_r()

screen.exitonclick()
>>>>>>> 1a4e32a (final)
