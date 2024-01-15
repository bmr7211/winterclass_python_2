import random
import turtle
t = turtle.Turtle()
t.shape("turtle")
#t.title("거북이 도장 찍기")

r = random.random()
g = random.random()
b = random.random()

x = random.randrange(-500, 500)
y = random.randrange(-500, 500)

for i in range(0, 20):
    r = random.random()
    g = random.random()
    b = random.random()

    x = random.randrange(-500, 500)
    y = random.randrange(-500, 500)

    a = random.randrange(0, 360)

    s = random.randrange(1, 10)

    t.up()
    t.left(a)
    t.shapesize(s)
    t.goto(x, y)
    t.color(r, g, b)
    t.stamp()
