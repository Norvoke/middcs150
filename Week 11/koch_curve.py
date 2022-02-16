"""
CS 150 Recursive Koch curve drawing 

"""

import sys
import turtle as t

def draw_koch(length, generation):
    """
    Recursive function to draw the Koch curve
    'length' is a integer representing the length of the segment to draw
    'generation' is an integer keeping track of the desired generation
    """
    if generation == 0:
        t.forward(length)
    else:
        draw_koch(length/2, generation - 1)
        t.left(60)
        draw_koch(length/2, generation - 1)
        t.left(60)
        draw_koch(length/2, generation - 1)
        t.left(60)
        draw_koch(length/2, generation - 1)
         
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 koch_curve.py <length> <generation>")
    else:
        t.tracer(False)     # to show drawing all at once
        # t.speed(0)        # to increase speed of the drawing a bit
        length = int(sys.argv[1])
        generation = int(sys.argv[2])
        t.penup(); t.backward(length//2); t.pendown()
        draw_koch(length, generation)
        t.update()
        t.done()
