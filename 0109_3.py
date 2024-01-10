'''
number = int(input('입력할 단: '))

for i in range(1, 10):
    summery = number * i
    print('{0} * {1} = {2}'.format(number, i, summery))


import turtle
t = turtle.Turtle()
t.shape("turtle")

s = int(input('몇각형? : '))

for i in range(s):
    t.fd(100)
    t.left(360 / s)
'''

import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

colors = ['red', 'orange', 'yellow', 'green', 'skyblue', 'blue', 'purple']

for i in colors:
    t.fillcolor(i)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.up()
    t.goto(random.randrange(-500, 500), (random.randrange(-500, 500)))
    t.down()






