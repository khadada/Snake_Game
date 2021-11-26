from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open('data.txt',mode='r') as f:
            self.high_score = int(f.read())
        self.score = 0
#       self.fetch_high_score()
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
#           self.update_high_score_data()
            with open('data.txt',mode="w") as f:
                f.write(f"{self.score}")
        self.score = 0
        self.clear()
        self.score_print()

#    def create_data(self):
#        with open('data.txt',mode='w') as f:
#            f.write(str(self.high_score))

#    def fetch_high_score(self):
#        with open('data.txt',mode='r') as f:
#            high_score = f.read()
#            self.high_score = int(high_score)

#    def update_high_score_data(self):
#        with open('data.txt',mode='w') as f:
#            f.write(str(self.high_score))

