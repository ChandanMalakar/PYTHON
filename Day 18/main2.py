from turtle import Turtle, Screen

tm = Turtle()

tm.shape("arrow")
tm.color("red", "black")

for _ in range(15):
    tm.forward(10)
    tm.up()
    tm.forward(10)
    tm.down()


screen = Screen()
screen.exitonclick()
