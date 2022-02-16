from turtle import *

def shape(x):
    for _ in range(4):
        forward(x)
        left(90)

side = 10
while side < 200:
    shape(side)
    side = side * 2