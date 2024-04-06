from turtle import Turtle, Screen


tm = Turtle()
screen = Screen()


def move_for():
    tm.forward(50)


def move_anti():
    new_heading = tm.heading() + 10
    tm.setheading(new_heading)
    # tm.left(10)


def move_clock():
    new_heading = tm.heading() - 10
    tm.setheading(new_heading)
    # tm.right(10)


def move_back():
    tm.backward(50)


def clear():
    tm.clear()
    tm.penup()
    tm.home()
    tm.pendown()


screen.listen()
screen.onkey(key="w", fun=move_for)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_anti)
screen.onkey(key='d', fun=move_clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
screen.onscreenclick(exit())