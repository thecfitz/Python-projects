# Colton Fitzjarrald (no other members)
# 11/4/18
# Ada Byron,the daughter of poet lord Byron wrote the first computer program, which calculated Bernoulli numbers in 1843
# Grace Hopper invented the computer compiler and coined the term computer bug.
# Katherine Johnson was a scientist who worked at NASA and calculated the trajectories of early space launches
# Shafi Goldwasser was a professor of electrical engineering and computer science at MIT
##########################

#first block is setting up the monitor
from random import randint
import turtle
wn = turtle.Screen()
wn.bgcolor('white')
tess = turtle.Turtle()
tess.penup()
#tess is the drawing code. It creates the lines.
tess.hideturtle()
tess.goto(-140, 140)
tess.color('black')
tess.pensize(2)
tess.speed(8)
tess.right(90)
# the first for loop of the block below writes the numbers above the lines, the second for loop creates the dashed lines.
for row in range(0, 15):
    tess.write(row)
    tess.forward(15)
    tess.pendown()
    for i in range(0, 11):
        tess.forward(7.5)
        tess.penup()
        tess.forward(7.5)
        tess.pendown()
    tess.penup()
    tess.goto((tess.xcor() + 25), 140)
# the next 4 blocks create the turtles, assigns their positions, and has them do rotations at start of race
ada = turtle.Turtle()
ada.hideturtle()
ada.pensize(.3)
ada.resizemode('auto')
ada.shape('turtle')
ada.color('red')
ada.penup()
ada.goto(-160, 100)
ada.showturtle()
ada.left(360)

grace = turtle.Turtle()
grace.hideturtle()
grace.pensize(.3)
grace.resizemode('auto')
grace.shape('turtle')
grace.color('purple')
grace.penup()
grace.goto(-160, 60)
grace.right(60)
grace.showturtle()
grace.right(300)

katherine = turtle.Turtle()
katherine.hideturtle()
katherine.pensize(.3)
katherine.resizemode('auto')
katherine.shape('turtle')
katherine.color('hotpink')
katherine.penup()
katherine.goto(-160, 20)
katherine.right(120)
katherine.showturtle()
katherine.left(480)

shafi = turtle.Turtle()
shafi.hideturtle()
shafi.pensize(.3)
shafi.resizemode('auto')
shafi.shape('turtle')
shafi.color('blue')
shafi.penup()
shafi.goto(-160, -20)
shafi.left(90)
shafi.showturtle()
shafi.right(450)
#the for loop below using the randint function to assign a distance travelled forward for each turtle, over 100 times.
for i in range(0, 100):
    ada.forward(randint(1, 6))
    grace.forward(randint(1, 6))
    katherine.forward(randint(1, 6))
    shafi.forward(randint(1, 6))

wn.mainloop()
