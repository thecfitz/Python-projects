# Colton Fitzjarrald (no other members)
# 10/28/18
##########################

import turtle
wn = turtle.Screen()
wn.bgcolor('turquoise')
wn.title('Hello, Tess!')

tess = turtle.Turtle()
tess.color('hot pink')
tess.pensize(10)
tess.shape('turtle')
tess.speed(1)

for m in range(1, 4):
    if m == 1:
        tess.forward(175)
        tess.penup()
    elif m == 2:
        tess.left(angle=120)
        tess.pendown()
        tess.forward(175)
        tess.penup()
    elif m == 3:
        tess.left(angle=120)
        tess.pendown()
        tess.forward(175)


wn.mainloop()
