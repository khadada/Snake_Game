from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=400, height=300)
screen.bgcolor('black')
screen.title('Snake Game')
screen.listen()
screen.tracer(0)    # stop tracer until the snake is ready
starting_postions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for postion in starting_postions:
    segment = Turtle()
    segment.shape('square')
    segment.color('white')
    segment.penup()
    segment.goto(postion)
    segments.append(segment)
game_is_on = True
while game_is_on:
    screen.update()      # because all segments in their position we update the screen
    time.sleep(0.5)      # here to wait the all segment take its new position
    for seg_num in range(len(segments)-1,0,-1):     # Here we reverse the range from last segment to the fist segment
        new_x = segments[seg_num - 1].xcor()        # Here I hold the next x cord for the last segment which is the second segment count from the last
        new_y = segments[seg_num - 1].ycor()        # Here I hold the next y cord for the last segment which is the second segment count from the last one
        segments[seg_num].goto(new_x,new_y)         # Here I set next position for last segment
        # The loop update the next position for each segment of the snake
        # Here we make the segments like associated together
    segments[0].forward(20)
    segments[0].left(90)




screen.exitonclick()
