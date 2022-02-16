"""
CS 150 examples for modules and constants
"""

import math
# from random import randint
# import random as r
from random import *
import turtle as t



SPEED_OF_LIGHT = 299792458

def triangle_area(base, height):
    area = base*height/2.0
    print("Area is: " + str(area))
    return area
 
# area = triangle_area(4, 5)
# print(area)

def lorentz(velocity):
    return 1 / (1 - (velocity ** 2) / (SPEED_OF_LIGHT ** 2)) ** 0.5

def lorentz(velocity):
    return 1 / math.sqrt(1 - (math.pow(velocity,2) / math.pow(SPEED_OF_LIGHT, 2)))

def roll():
    return r.randint(1,6)

def rectangle(sidelen):
    t.forward(sidelen)
    t.left(90)
    t.forward(sidelen)
    t.left(90)
    t.forward(sidelen)
    t.left(90)
    t.forward(sidelen)
    t.left(90)
    
def jumpto(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def generate_picture():
    jumpto(-100, -100)
    t.fillcolor("blue")
    t.begin_fill()
    rectangle(200)
    t.end_fill()
    jumpto(200, 200)
    t.fillcolor("#00ffff")
    t.begin_fill()
    rectangle(100)
    t.end_fill()
    
    