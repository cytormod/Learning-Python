from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# segments = []
#
# for position in starting_positions:
#     new_segment = Turtle('square')
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # for seg in segments:
    #     seg.forward(20)
    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)
    # segments[0].left(90)


    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    #If head collides with any segment in the tail:
        #trigger game_over






screen.exitonclick()