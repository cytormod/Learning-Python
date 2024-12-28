import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tupple_color = (r, g, b)
    return tupple_color

random_color()

# direction = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))


def draw_spirograph(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        # tim.pensize(5)
        tim.setheading((tim.heading() + size_of_gap))

draw_spirograph(5)

tim.shape("turtle")
screen = t.Screen()
screen.exitonclick()