import turtle as t
import random as r

red_count = 5
green_count = 0
blue_count = 0
def sierpinski_carpet(length, levels):
    global red_count, green_count, blue_count
    t.colormode(255)
    if levels == 0:
        red = r.randint(0,160)
        green = r.randint(0,160)
        blue = r.randint(0,160)
        t.color(red_count, green_count, blue_count)
        if red_count >= 250:
            red_count = 0
            green_count = 5
        if green_count >= 250:
            green_count = 0
            blue_count = 5
        if blue_count >= 250:
            blue_count = 0
            red_count = 5
        if red_count > 0:
            red_count += 10
        if green_count > 0:
            green_count += 10
        if blue_count > 0:
            blue_count += 10
        t.begin_fill()
        for _ in range (4):
            t.forward(length)
            t.left(90)
        t.end_fill()
    else:
        for _ in range(4):
            sierpinski_carpet(length/3, levels-1)    
            t.forward(length/3)
            sierpinski_carpet(length/3, levels-1)    
            t.forward(length/3)
            t.forward(length/3)
            t.left(90)