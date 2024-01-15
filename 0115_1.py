import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

colors = ['red', 'orange', 'yellow', 'green', 'skyblue', 'blue', 'purple']
length = 5

t.speed(0)
turtle.bgcolor("black")

x = random.randrange(-500, 500)
y = random.randrange(-500, 500)

t.goto(x, y)

for i in range(1, 201):
    t.pencolor(colors[i % 7])
    t.fd(i)
    t.left(45)
        #length += 1
