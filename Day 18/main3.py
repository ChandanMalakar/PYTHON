from turtle import Turtle, Screen
import random
tm = Turtle()
tm.shape("arrow")


# def loop(color, ran, r):
#     tm.color(color)
#     for _ in range(ran):
#         tm.forward(100)
#         tm.right(r)
#
#
# def triangle():
#     loop("cyan", 3, 120)
#     square()
#
#
# def square():
#     loop("burlywood4", 4, 90)
#     pentagon()
#
#
# def pentagon():
#     loop("brown", 5, 72)
#     hexagon()
#
#
# def hexagon():
#     loop("red", 6, 60)
#     heptagon()
#
#
# def heptagon():
#     loop("cadetblue4", 7, 51.42)
#     octagon()
#
#
# def octagon():
#     loop("orange", 8, 45)
#     nonagon()
#
#
# def nonagon():
#     loop("indigo", 9, 40)
#     decagon()
#
#
# def decagon():
#     loop("violet", 10, 36)
#
#
# triangle()

# Above one is my code , below one is what I learnt

colors = ["cyan", "burlywood4", "brown", "red", "cadetblue4", "orange", "indigo", "violet"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    tm.color(random.choice(colors))
    for _ in range(num_sides):
        tm.forward(100)
        tm.right(angle)


for i in range(3, 11):
    draw_shape(i)

screen = Screen()
screen.exitonclick()
