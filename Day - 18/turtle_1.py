import turtle as t
import random

kayo = t.Turtle()
t.colormode(255)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range (num_sides):
        kayo.forward(100)
        kayo.right(angle)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

for shape_sides_n in range(3,11):
    kayo.color(random_color())
    draw_shape(shape_sides_n)