from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("arial", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("arial", 50, "normal"))

    def add_score_l(self):
        self.clear()
        self.l_score += 1

    def add_score_r(self):
        self.clear()
        self.r_score += 1
