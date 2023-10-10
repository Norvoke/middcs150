"""
CSCI 150 Lab 9 Fractals

Draws a few patterns using recursive turtle commands to create some common fractals including:
A descending stairway, sierpenski's triangles and carpet(with colors), and an H with fractal serifs.

Name: Finn Ellingwood
Section: B

Creativity: I created a function to draw sierpenski's carpet that fills the colors of the squares
by cycling through red, green, and blue to create patterns flowing from black to bright red, green
or blue.

"""

import turtle as t
import random as r

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def stairs(length, levels):
    """
    A recursive turtle function drawing a set of descending stairs.
    
    Args:
        length: How wide the first stair would be drawn in pixels
        levels: Number of levels deep the resursion should go, higher -> longer run time
        
            Note: The once the level reaches 6 on a starting length of 100, the stair will
            only be about 3 pixels, so any more levels will just add to the run time without
            draw
        
    Returns:
        Nothing
    """
    if levels > 0:
        t.forward(length)
        t.right(90)
        t.forward(length)
        t.left(90)
        stairs(length/2, levels-1)
        t.forward(-length)
        t.right(90)
        t.forward(-length)
        t.left(90)

def sierpinski(length, generation):
    """
    A recursive turtle function drawing sierpinski's triangles.
    
    Args:
        length: How wide the generation 0 triangle would be drawn in pixels
        
        levels: Number of levels deep the resursion should go, higher -> longer run time
        
    Returns:
        Nothing
    """
    if generation > 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
            sierpinski(length/2, generation-1)
            
def recursive_h(length, level):
    """
    A recursive turtle function which draws an H that has fractal serifs.
    
    Args:
        length: half as wide as the base of the H will be.
        levels: Number of levels deep the resursion should go, higher -> longer run time
        
    Returns:
        Nothing
    """
    if level > 0:
        t.forward(length)
        t.left(90)
        t.forward(length/2)
        t.right(90)
        recursive_h(length/2, level-1)
        t.left(90)
        t.forward(-length)
        t.right(90)
        recursive_h(length/2, level-1)
        t.left(90)
        t.forward(length/2)
        t.right(90)
        t.forward(-2*length)
        t.left(90)
        t.forward(length/2)
        t.right(90)
        recursive_h(length/2, level-1)
        t.left(90)
        t.forward(-length)
        t.right(90)
        recursive_h(length/2, level-1)
        t.left(90)
        t.forward(length/2)
        t.right(90)
        t.forward(length)
    if level == 0: # base case
        t.dot(5)

# defining some global variables to be used in the coloring of the carpet
red_count = 5
green_count = 0
blue_count = 0
def sierpinski_carpet(length, levels):
    """
    A recursive turtle function drawing a colored sierpinski's carpet.
    
    Args:
        length: How wide the level 0 cube would be drawn in pixels
        levels: Number of levels deep the resursion should go, higher -> longer run time
        
    Returns:
        Nothing
    """
    global red_count, green_count, blue_count
    t.colormode(255)
    if levels == 0: # base case
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

def drawing_demo():
    """
    Create drawings of `stairs`, `sierpinski`, and `recursive_h`.
    
    Args:
        None
    """
    t.tracer(False)
    
    # draw stairs in upper left of drawing window
    t.penup()
    t.goto(-t.window_width()/2 + 20, t.window_height()/2 - 20)
    t.pendown()    
    stairs(150, 6)
       
    # draw sierpinski in upper right of drawing window
    t.penup()
    t.goto(0, t.window_height()/2 - 300)
    # t.goto(0,40)
    t.pendown()    
    sierpinski(300, 5)
    
    # draw recursive H in lower half of drawing window
    t.penup()
    t.goto(0, -t.window_height()/4)
    t.pendown()
    recursive_h(150, 4)
    
    # draw recursive H in lower half of drawing window
    t.penup()
    t.goto(0, -t.window_height()/10)
    t.pendown()
    sierpinski_carpet(200, 3)
    #recursive_h(150, 4)
    
    
    # finish
    t.update() 
    t.done()     
