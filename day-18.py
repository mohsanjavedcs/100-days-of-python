# import colorgram

# rgb_colours = []
# colours = colorgram.extract("_hirst.jpg", 30)

# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)

# print(rgb_colours)
import turtle as t
import random as r

t.colormode(255)
zee = t.Turtle()
colour_list = [(198, 173, 119), (214, 225, 218), (222, 224, 229), (162, 99, 55), (126, 35, 23), (185, 158, 50), (5, 55, 83), (51, 33, 29), (110, 69, 86), (116, 163, 176), (22, 121, 171), (76, 34, 43), (66, 153, 131), (84, 140, 63), (7, 65, 45), (127, 36, 41), (184, 97, 80), (204, 200, 146), (144, 178, 165), (172, 151, 156), (179, 201, 187), (215, 182, 173), (25, 80, 60), (13, 80, 101), (79, 147, 165), (162, 105, 111), (203, 184, 187), (177, 197, 203)]

zee.speed("fastest")
zee.penup()
zee.hideturtle()
zee.setheading(225)
zee.forward(300)
zee.setheading(0)
number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    zee.dot(20, r.choice(colour_list))
    zee.forward(50)

    if dots % 10 == 0:
        zee.setheading(90)
        zee.forward(50)
        zee.setheading(180)
        zee.forward(500)
        zee.setheading(0)

screen = t.Screen()
screen.exitonclick()