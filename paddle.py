from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cor[0], cor[1])

    # function for the movement of the Paddles:
    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        # while self.ycor() > -240:
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
