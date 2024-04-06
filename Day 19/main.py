import turtle
from turtle import Turtle, Screen

tm = turtle.Turtle()
screen = Screen()


def forward():
    tm.forward(20)


screen.listen()
screen.onkey(key="space", fun=forward)
screen.exitonclick()
