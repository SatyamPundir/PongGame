import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.mov_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce_wall(self):
        print("Wall")
        self.y_cor *= -1

    def bounce_paddle(self):
        print("padle")
        self.x_cor *= -1
        self.mov_speed *= 0.9

    def reset(self):
        self.mov_speed = 0.1
        self.goto(0, 0)
        self.x_cor *= -1

    def inc_speed(self):

        self.x_cor += 5
        self.y_cor += 5
