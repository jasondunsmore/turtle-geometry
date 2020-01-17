#!/usr/bin/env python

import turtle
turtle.setup(width=600, height=600, startx=None, starty=None)
t = turtle.Turtle()

def squarepiece(size):
    t.forward(size)
    t.right(90)

def square(size):
    for i in range(4):
        squarepiece(size)

def rectangle(side1, side2):
    for i in range(2):
        squarepiece(side1)
        squarepiece(side2)

def try_angle(size):
    for i in range(3):
        t.forward(size)
        t.right(60)

def triangle(size):
    for i in range(3):
        t.forward(size)
        t.right(120)

def house(side):
    t.left(90)
    square(side)
    t.forward(side)
    t.right(30)
    triangle(side)

def thing():
    for dist in [100, 100, 50, 50, 100, 25, 25]:
        t.forward(dist)
        t.right(90)
    t.forward(50)

def thing1():
    for i in range(4):
        thing()

def thing2():
    for i in range(15):
        thing()
        t.right(10)
        t.forward(50)

def thing3():
    for i in range(15):
        thing()
        t.left(45)
        t.forward(100)

def circle(size):
    for i in range(360):
        t.right(1)
        t.forward(size)

def arcr(r, deg):
    for i in range(deg):
        t.forward(r)
        t.right(1)

def arcl(r, deg):
    for i in range(deg):
        t.forward(r)
        t.left(1)

