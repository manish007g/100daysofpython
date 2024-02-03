import colorgram
from turtle import *
import random
colormode(255)
# colors = colorgram.extract('hirst.jpg', 50)
# rgb_colors= []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r, g, b)
#     rgb_colors.append(new_color)

colors_list= [(0, 0, 0), (238, 237, 234), (150, 143, 139), (124, 112, 110), (230, 241, 234), (122, 160, 205), (48, 101, 159), (139, 65, 89), (242, 232, 236), (243, 76, 34), (227, 234, 241), (242, 205, 78), (49, 132, 64), (217, 122, 149), (229, 77, 100), (122, 194, 149), (193, 148, 51), (55, 166, 132), (127, 220, 187), (55, 51, 128), (102, 103, 174), (245, 159, 149), (17, 103, 45), (253, 200, 0), (62, 46, 56), (44, 32, 68), (99, 90, 7), (125, 41, 48), (156, 216, 223), (232, 167, 179), (47, 67, 55), (127, 42, 35), (172, 185, 222), (80, 151, 164)]
timmy = Turtle()

shift = 50
#print(timmy.position())



for i in range (1, 12):
    timmy.pu()
    timmy.setposition(-300, (-330+shift))
    shift += 50
    timmy.pd()
    color_selected = random.choice(colors_list)
    timmy.dot(20, color_selected)
    for _ in range(1, 12):
        timmy.pu()
        timmy.forward(50)
        color_selected = random.choice(colors_list)
        timmy.dot(20, color_selected)
        timmy.pd()

timmy.ht()





screen = Screen()
screen.exitonclick()