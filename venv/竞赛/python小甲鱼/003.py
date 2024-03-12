# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/16 9:33'

import turtle

t = turtle.Pen()
colors = ("red", "blue", "green", "black", "yellow", "pink", "purple")

for i in range(10):
    t.penup()
    t.goto(0, -i * 10)
    t.pendown()
    t.color(colors[i % 7])
    t.circle(15+i*10)

turtle.done()
