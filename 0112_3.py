import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

colors = ['red', 'yellow', 'green', 'blue', 'purple']
fillcolors = ['grey', 'black', 'white', 'beige']
'''
t.pensize(30)
for i in colors:
    t.pencolor(i)
    t.circle(100, 360/7)

for i in colors:
    t.pencolor(i)
    for i in range(5):
        t.fd(100)
        t.left(144)
    t.up()    
    t.goto(random.randrange(-500, 501), random.randrange(-500, 501))
    t.down()

t.pensize(10)
for i in colors:
    t.pencolor(i)
    t.fd(150)
    t.left(360/7)
'''
n = int(input('횟수: '))

t.pensize(5)
for i in range(n):
    for i in range(5):
        for i in colors:
            t.pencolor(i)
            t.fd(50)
        t.left(144)

    t.up()    
    t.goto(random.randrange(-500, 501), random.randrange(-500, 501))
    t.down()
'''
t.shapesize(2, 2)
t.color(colors[i], fillcolors[i])
t.stamp()
t.fd(100)
t.stamp
'''
