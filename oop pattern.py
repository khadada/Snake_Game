from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=400, height=300)
screen.bgcolor('black')
screen.title('Snake Game')
screen.listen()
screen.tracer(0)    # stop tracer until the snake is ready
snake = Snake()
game_is_on = True
while game_is_on:
    screen.update()      # because all segments in their position we update the screen
    time.sleep(0.5)      # here to wait the all segment take its new position
    snake.move()


screen.exitonclick()
