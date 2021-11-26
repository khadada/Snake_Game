from turtle import Screen
from snake import Snake
import time
from food import Food
from score_module import Score
screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)    # stop tracer until the snake is ready
score = Score()
score.fetch_high_score()
snake = Snake()
food = Food()
game_is_on = True
screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
while game_is_on:
    screen.update()      # because all segments in their position we update the screen
    time.sleep(0.3)      # here to wait the all segment take its new position
    snake.move()
    score.fetch_high_score()

    if snake.head.distance(food) < 15:
        print("hom hom hom")
        food.refresh()
        score.score_up()
        snake.grow_up()
    if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        # game_is_on = False
        snake.reset_snake_position()
        score.reset_score()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            # score.game_over()
            # game_is_on = False
            score.reset_score()
            snake.reset_snake_position()


screen.exitonclick()
