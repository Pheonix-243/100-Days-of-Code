##This code will not work in repl.it as there is no access to the colorgram package here.###
#We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
kayo = turtle_module.Turtle()
kayo.speed("fastest")
kayo.penup()
kayo.hideturtle()

colors = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
    (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
    (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
    (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
    (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
    (176, 192, 208), (168, 99, 102)
]

kayo.setheading(225)
kayo.forward(300)
kayo.setheading(0)

num_of_dots = 100
dot_size = 20
spacing = 50

for dot_count in range(1, num_of_dots + 1):
    kayo.dot(dot_size, random.choice(colors))
    kayo.forward(spacing)

    if dot_count % 10 == 0:
        kayo.setheading(90)
        kayo.forward(spacing)
        kayo.setheading(180)
        kayo.forward(spacing * 10)
        kayo.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
