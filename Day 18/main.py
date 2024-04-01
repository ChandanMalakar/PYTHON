import turtle
from turtle import Turtle, Screen
import heroes

# from turtle module importing Turtle & Screen class

# creating object of the Turtle class
timmy_the_turtle = Turtle()

# to learn about this library module , everyone should go through the documentation of that file

# changing shape to the default turtle symbol -> pointer to a "turtle".
timmy_the_turtle.shape("turtle")

timmy_the_turtle.color("black", "green")

# moving the turtle by 100 pases

# timmy_the_turtle.forward(100)


# moving the turtle in terms of angle
for i in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)

for _ in range(4):
    timmy_the_turtle.backward(100)
    timmy_the_turtle.left(90)

# creating obj of the Screen class
screen = Screen()
screen.exitonclick()

print(heroes.gen())
print(heroes.genarr(3))
