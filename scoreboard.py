from turtle import Turtle

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 250)
        self.write(self.score_l, False, font=("courier", 25, "normal"))
        self.goto(50, 250)
        self.write(self.score_r, False, font=("courier", 25, "normal"))

    def left_score(self):
        self.score_l += 1
        self.update_scoreboard()

    def right_score(self):
        self.score_r += 1
        self.update_scoreboard()


