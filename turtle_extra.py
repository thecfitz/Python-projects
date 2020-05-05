# Colton Fitzjarrald
# 10/28/18
#########################

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(2)
alex.color('turquoise')
alex.pendown()

for i in range(1, 11):
    alex.forward(100)
    alex.left(90)
    alex.forward(100)
    alex.left(90)
    alex.forward(100)
    alex.left(90)
    alex.forward(100)
    alex.left(126)

wn.mainloop()
