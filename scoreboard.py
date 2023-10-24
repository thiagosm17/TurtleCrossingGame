from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-220, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", False, "center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", font=('Courier', 30, 'normal'))

