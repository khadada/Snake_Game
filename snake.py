from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.setup()

    def setup(self):
        for position in STARTING_POSITION:
            segment = Turtle()
            segment.shape('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for num_seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[num_seg - 1].xcor()
            new_y = self.segments[num_seg - 1].ycor()
            self.segments[num_seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_STEP_DISTANCE)
