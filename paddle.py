from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__("square")
        self.x = x_cor
        self.y = y_cor
        self.color("white")
        self.penup()
        self.speed('fastest')
        self.shapesize(6, 1)
        self.goto(self.x, self.y)

    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.x, new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.x, new_y)

    def move_randomly(self):
        self.tut.speed("slowest")
        while self.tut.ycor() < 220:
            new_y = self.tut.ycor() + 20
            self.tut.goto(-350, new_y)
            if self.tut.ycor() == 220:
                while self.tut.ycor() > -220:
                    new_y = self.tut.ycor() - 20
                    self.tut.goto(-350, new_y)
            elif self.tut.ycor() == -220:
                while self.tut.ycor() < 220:
                    new_y = self.tut.ycor() + 20
                    self.tut.goto(-350, new_y)

