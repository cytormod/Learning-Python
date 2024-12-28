from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

# def movement(key):
#     if key =="w":
#         tim.forward(10)
#     elif key == "s":
#         tim.backward(10)
#     elif key == "a":
#         tim.left(90)
#     elif key == 'd':
#         tim.right(90)
#     elif key =='c':
#         tim.setx(0), tim.sety(0)
#
# movement(screen.onkey)

def mov_forwards():
    tim.forward(10)
def mov_backwards():
    tim.backward(10)
def mov_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
def mov_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=mov_forwards)
screen.onkey(key="s", fun=mov_backwards)
screen.onkey(key="a", fun=mov_left)
screen.onkey(key="d", fun=mov_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()