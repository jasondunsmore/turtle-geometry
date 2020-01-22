#!/usr/bin/env python

import turtle
turtle.setup(width=600, height=600, startx=None, starty=None)
turtle.delay(0)
t = turtle.Turtle()

def reset():
    turtle.Screen().reset()

def squarepiece(size=10):
    t.forward(size)
    t.right(90)

def square(size=10):
    for i in range(4):
        squarepiece(size)

def rectangle(side1=10, side2=10):
    for i in range(2):
        squarepiece(side1)
        squarepiece(side2)

def try_angle(size=10):
    for i in range(3):
        t.forward(size)
        t.right(60)

def triangle(size=10):
    for i in range(3):
        t.forward(size)
        t.right(120)

def house(side=10):
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

def circle(size=1):
    for i in range(360):
        t.right(1)
        t.forward(size)

def circlething(i=30):
    for i in range(i):
        circle(i+1)
        circle(-i+1)

def arcr(r, deg):
    for i in range(deg):
        t.forward(r)
        t.right(1)

def arcl(r, deg):
    for i in range(deg):
        t.forward(r)
        t.left(1)

def trianglething(deg=10, start=1, end=100, inc=1):
    i = start
    while i <= end:
        triangle(i)
        i += inc
        t.right(deg)

def spiderweb(start=1, end=200, inc=5):
    i = start
    # Draw lines to make web on
    for i in range(6):
        t.forward(500)
        t.setpos(0,0)
        t.right(60)
    # Draw web
    while i <= end:
        triangle(i)
        i += inc
        t.right(60)

def bubble(deg=50):
    while True:
        circle()
        t.right(deg)

def torus(size=20, deg=22):
    while True:
        circle(2)
        t.forward(size)
        t.right(deg)

def petal(size=5):
    arcr(size, 60)
    t.right(120)
    arcr(size, 60)
    t.right(120)

def flower(size=5):
    for i in range(6):
        petal(size)
        t.right(60)

def starburst(i=1):
    flower(i)
    starburst(i+1)

def rectangle1(deg=50):
    while True:
        rectangle(10, 50)
        t.forward(100)
        t.right(deg)

def windmill():
    rectangle1(200)
