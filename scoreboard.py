from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_point = 0
        self.r_point = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_point, align="center", font=("courier", 20, "normal"))
        self.goto(100, 200)
        self.write(self.r_point, align="center", font=("courier", 20, "normal"))

    def score_l(self):
        self.l_point += 1
        self.update()

    def score_r(self):
        self.r_point += 1
        self.update()
