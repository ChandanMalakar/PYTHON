from turtle import Turtle, Screen
import random

screen = Screen()
tm = Turtle()
# colors = ["cyan", "burlywood4", "brown", "red", "cadetblue4", "orange", "indigo", "violet"]
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tm.speed(0)
tm.pensize(10)
for _ in range(200):
    # tm.color(random.choice(colors))
    tm.color(random_color())
    tm.forward(30)
    tm.seth(random.choice(directions))

screen.screensize(2000, 2000)
screen.screensize()
screen.exitonclick()
