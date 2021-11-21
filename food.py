from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        random_x = randint(-240, 240)
        random_y = randint(-220, 220)
        self.goto(random_x, random_y)
