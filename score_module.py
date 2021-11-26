from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.high_score = 0
        self.score = 0
        self.score_print()

    def score_print(self):
        self.goto(0, 300)
        self.color('white')
        self.write(f"Score: {self.score}         High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.score_print()


 #   def game_over(self):
        #       print('game over'.title())
        #        self.goto(0,0)
#       self.write("Game over ", align=ALIGNMENT, font=FONT)
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.score_print()

