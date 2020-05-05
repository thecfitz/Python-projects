# Colton Fitzjarrald (no other members)
# 10/28/18
########################

import turtle
wn = turtle.Screen()
wn.bgcolor('turquoise')

tess = turtle.Turtle()
colors = ['yellow', 'red', 'purple', 'blue']
tess.pensize(10)
tess.shape('turtle')
tess.speed(1)

for m in range(1, 5):
    if m == 1:
        tess.color(colors[0])
        tess.forward(200)
        tess.penup()
    elif m == 2:
        tess.color(colors[1])
        tess.left(angle=90)
        tess.pendown()
        tess.forward(200)
        tess.penup()
    elif m == 3:
        tess.color(colors[2])
        tess.left(angle=90)
        tess.pendown()
        tess.forward(200)
        tess.penup()
    elif m == 4:
        tess.color(colors[3])
        tess.left(angle=90)
        tess.pendown()
        tess.forward(200)

wn.mainloop()
