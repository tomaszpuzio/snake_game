from turtle import Turtle

POSITION_X = 0
POSITION_Y = 230
ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(POSITION_X, POSITION_Y)
        self.hideturtle()
        self.print_score()

    def update_l_score(self):
        self.clear()
        self.l_score += 1
        self.clear()
        self.print_score()

    def update_r_score(self):
        self.clear()
        self.r_score += 1
        self.print_score()

    def print_score(self):
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)