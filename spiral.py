# Colton Fitzjarrald (no other members)
# 10/28/18
######################

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.penup()
alex.shape('turtle')

for pink in range(5, 60, 2):
    alex.color('hotpink')
    alex.forward(pink)
    alex.stamp()
    alex.left(24)
for turq in range(5, 60, 2):
    alex.color('turquoise')
    alex.forward(turq)
    alex.stamp()
    alex.left(24)
for purp in range(5, 60, 2):
    alex.color('purple')
    alex.forward(purp)
    alex.stamp()
    alex.left(24)
for blue in range(5, 60, 2):
    alex.color('blue')
    alex.forward(blue)
    alex.stamp()
    alex.left(24)

wn.mainloop()
