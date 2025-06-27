# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:30:06 2023

@author: HP
"""
import turtle as t
def drawfib(n, len_ang):
    t.forward(2 * len_ang)
    if n == 0:
        pass# // Do nothing.
    elif n == 1:
        pass# // Do nothing.
    else:
        t.left(len_ang)
        drawfib(n - 1, len_ang)
        t.right(2 * len_ang)
        drawfib(n - 2, len_ang)
        t.left(len_ang)
    t.backward(2 * len_ang)
# Six different starting points for six different trees.
start_points = [[-300, 250], [-150, 250],
                [-300, 110], [-80, 110],
                [-300, -150], [50, -150]]

# For each starting point, draw a tree with n varying
# between 1 and 6 and len_ang set to 30.
n = 0
# for start_point in start_points:
#     x, y = start_point
#     n = n + 1

#     t.penup()
#     t.setpos(x, y)
#     t.pendown()
#     drawfib(n, 30)
t.reset()
t.bgcolor('black')
t.pensize(3)
t.setpos(-330,-160)
t.tracer(0, 0)
def ks(length, d):
    if d == 0:
        t.forward(length)
    else:

        length = length / 3
        d = d - 1
        ks(length*1.5, d)
        t.right(60)
        ks(length*1.5, d)
        t.left(120)
        ks(length*1.5, d)
        t.right(60)
        ks(length*1.5, d)

colors = ["red", "orange"]
for i in range(2):
    t.color(colors[i])
    ks(200, 3)

# 330 CHAPTER 13. TURTLE GRAPHICS
    t.left(120)
t.pensize(8)
t.color('cyan')
ks(200, 3)
t.update()
t.tracer(1, 10)

t.done()