# 원 테두리, 채우는 색 랜덤

import random
colors = ['red' , 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
import turtle
t = turtle.Turtle()
t.shape("turtle")

n1 = random.randrange(7)
n2 = random.randrange(7)

t.pencolor(colors[n1])
t.fillcolor(colors[n2])
t.begin_fill()
t.circle(100)
t.end_fill()
