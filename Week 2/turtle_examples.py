"""
CS 150 class examples of turtle functions, for loops, random numbers
"""

# NOTE: If you call these functions from the shell, the drawing window pops up.
# Use "t.clear()" to clear the window of any drawings, and "t.bye()" to close the
# window. The latter may require you to restart the Python shell (with the stop
# sign) to start drawing again.

import turtle as t
from random import randint

def square(length):
    """ Draw a square with sides of length """
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    
def iterative_square(length):
    """ Draw a square with sides of length using a loop """
    for _ in range(4):
        t.forward(length)
        t.right(90)

def simple_star():
    """ Draw a star """
    for _ in range(36):
        t.forward(100)
        t.backward(100)
        t.right(10)

def asterisk_star(length, spokes):
    """ Draw an asterisk star with spokes number of spokes of length length """
    angle = 360/spokes
    for _ in range(spokes):
        t.forward(length)
        t.backward(length)
        t.right(angle)        
        
def simple_spiral():
    """ Draw a spiral """
    for i in range(50):
        t.forward(i*5)
        t.right(55)
        
# A good example is side = 200 and angle = 89
def spiral(sides, angle):
    """ Draw spiral with sides steps and update of angle """
    for i in range(sides):
        t.forward(i*5)
        t.right(angle)
    
def rotating_circles(radius, num):
    """ Draw num rotating circles with radius """
    angle = 360/num
    for _ in range(num):
        t.circle(radius)
        t.right(angle)

def scribble(num_lines):
    """ Randomly draw num_lines lines """
    for _ in range(num_lines):
        x = randint(-100,100)
        y = randint(-100,100)
        t.goto(x,y)
        
def walk(num_steps, step_size):
    """ Random walk with num_steps steps of step_size """
    for _ in range(num_steps):
        angle = randint(-90, 90)
        t.right(angle)
        t.forward(step_size)

def pretty_picture():
    """ Draw random stars """
    for _ in range(10):
        # Get some random values
        spokes = randint(5, 30)
        length = randint(10, 60)
        angle = randint(-90,90)
        move = randint(20, 100)

        # Move randomly somewhere else
        t.right(angle)
        t.forward(move)
        
        # Draw a random star there
        asterisk_star(length, spokes)
        
def golden_spiral(radius, segments):
    """
    Draw a Fibonacci spiral using Turtle. turtle module must be imported into namespace.
    
    Args:
        radius: Starting radius of the spiral
        segments: Number of quarter circle segments to draw after initial quarter circle.
            Must be >= 2.
    
    Returns:
        None
    """
    a = radius
    t.circle(a, 90)    
    b = radius
    t.circle(b, 90)    
    for _ in range(segments-2): # segments-2 since first two segments already drawn
        c = a + b        
        t.circle(c, 90)
        # Prepare for the next iteration of the loop
        a = b
        b = c

def generate_picture():
#    t.tracer(False)
    spiral(200, 89)
    t.home
    scribble(num_lines)
#    t.done()