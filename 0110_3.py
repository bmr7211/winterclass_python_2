import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

number = int(input('횟수: '))

for i in range(number):
    for j in range(2):
        t.circle(120, 60)
        t.left(120)
    t.left(360 / number)
