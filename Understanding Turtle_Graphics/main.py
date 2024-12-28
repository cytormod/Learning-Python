from turtle import Turtle, Screen
import random
# from turtle import * # Here it is importing everything, from the turtle Module
# import turtle as t # Here we are changing the ClassName to t, just to write in short
# tim = t.Turtle()


tim = Turtle()
tim.shape("turtle")
tim.color('red')
colors = ["CornflowerBlue", "aquamarine", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(0,4):
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range (15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# ---------------------

# angles = 2
# for _ in range(0, 8):
#     angles +=1
#     print(angles)
#     for _ in range(angles):
#         tim.forward(100)
#         tim.right(360/angles)

# ================================

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     tim.pensize(10)
#     draw_shape(shape_side_n)

# ============================

directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("slow")
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
































screen = Screen()
screen.exitonclick()





