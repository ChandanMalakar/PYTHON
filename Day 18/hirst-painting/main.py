from turtle import Turtle, Screen
# import colorgram
import random
screen = Screen()
tm = Turtle()
screen.colormode(255)
# rgb_colors = []
# colors = colorgram.extract("img.png", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(239, 239, 237), (235, 229, 232), (231, 236, 232), (234, 35, 108), (237, 74, 34), (154, 27, 61), (6, 148, 94), (215, 229, 234), (234, 168, 39), (183, 158, 45), (26, 126, 194), (43, 191, 230), (85, 27, 92), (253, 223, 0), (125, 193, 73), (241, 219, 61), (180, 40, 101), (65, 175, 100), (212, 131, 166), (211, 58, 29)]

tm.speed(0)
tm.up()
tm.hideturtle()
tm.setheading(225)
tm.forward(300)
tm.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots + 1):
    tm.dot(20, random.choice(color_list))
    tm.forward(50)
    if i % 10 == 0:
        tm.setheading(90)
        tm.forward(50)
        tm.setheading(180)
        tm.forward(500)
        tm.setheading(0)


screen.screensize(2000, 2000)
screen.screensize()
screen.exitonclick()
