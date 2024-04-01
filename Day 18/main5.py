from turtle import Turtle, Screen
import random
tm = Turtle()
screen = Screen()
tm.speed(0)
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


current_heading = tm.heading()
tm.setheading(current_heading + 10)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tm.color(random_color())
        tm.circle(100)
        tm.setheading(tm.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
