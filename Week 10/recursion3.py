"""
CS 150 recursion examples with turtle
"""

import turtle as t

def spiral1(length, levels):
    """
    Draw a spiral with 'levels' segments with initial 'length' 
    """
    # Implicit base case: do nothing if levels == 0
    if levels > 0:
        t.forward(length)
        t.left(10)
        spiral1(0.999 * length, levels-.6) # Recurse
        
# spiral1(80, 40)


def spiral2(length, levels):
    """
    Draw a spiral with 'levels' segments with initial 'length'
    and return to starting position
    """
    # Implicit base case: do nothing if levels == 0
    if levels > 0:
        t.forward(length)
        t.left(30)
        spiral2(0.95 * length, levels-1) # Recurse 
        t.right(30) # Reverse the movements
        t.backward(length)
        
# spiral2(80, 40)


def draw_tree(length, levels):
    """
    Draw a recursive tree and return to where the turtle started
    Args:
        length: length of initial tree trunk
        levels: number of tree trunk segments from bottom to top
    """
    if levels > 0:
        t.forward(length)                  # draw tree branch
        t.right(10)
        draw_tree(length/2, levels-1)      # draw right subtree
        t.left(10*2)                       # undo right turn, then turn left again
        draw_tree(length/2, levels-1)      # draw left subtree
        t.right(10)                        # undo left turn
        t.backward(length)                 # trace back down the tree branch

def tree_demo(length, levels):
    """
    Move to bottom of drawing window and call recursive function to draw tree
    Args:
        length: length of initial tree trunk
        levels: number of tree trunk segments from bottom to top

    """
    t.tracer(1, 10)  # Control animation: fast with tracer(False); slow with tracer(1,10)
    t.penup()
    t.goto(0, -t.window_height()/2 + 50)
    t.left(90)
    t.pendown()    

    # draw the tree by calling our recursive drawing function
    draw_tree(length, levels)

    # finished
    t.update()
    t.done()

# tree_demo(200, 5)


def broccoli(length):
    """ 
    Draw a recursive broccoli and return to where the turtle started    
    Args:
        length: Stem length        
    Returns:
        Number of lines drawn
    """
    if length < 10:
        t.dot("yellow")
        return 0
    else:
        # Draw the stem
        t.pencolor("green")
        t.forward(length)
        lines = 1
        
        # Draw three broccolis with shorter stems      
        t.left(20)
        lines += broccoli(length * 0.75)
        t.right(20)
        lines += broccoli(length * 0.75)
        t.right(20)
        lines += broccoli(length * 0.75)
        t.left(20)
        
        # Return to starting position
        t.backward(length)
        return lines
         

def broccoli_demo(length):
    """
    Generate a good looking broccoli
    Args:
        length: Stem length
    """
    # Control animation speed
    t.tracer(100, 0)
    
    # Move the turtle to bottom of drawing window, pointing up
    t.pu()
    t.goto(0, -200)
    t.setheading(90)  
    t.pd()
    
    # draw the broccoli figure and record how many lines were drawn
    lines = broccoli(length)
    print('Drew ' + str(lines) + ' lines')
    
    # finished
    t.update()
    t.done()

# broccoli_demo(90)


# -----------------------------------------------
# Just for fun, draw trees where mouse is clicked
def tree_demo_click(length, start_level):
    """
    Draws increasingly complex trees rooted at each mouse click
    Args:
        length: length of initial tree trunk
        start_level: first tree level

    """
    global levels
    screen = t.Screen()
    t.tracer(1,100)  # Control animation: fast with tracer(False); slow with tracer(1,10)
    t.penup()
    levels = start_level
    
    def tree_click(x, y):
        global levels
        # jump the turtle to the mouse click location
        t.goto(x, y)       
        t.seth(90)
        t.pendown()
        draw_tree(length, levels)
        # increment complexity of next tree
        levels += 1        
        t.penup()

    # draw a tree where mouse was clicked
    screen.onclick(tree_click)    

    t.update()
    t.done()
    
# tree_demo_click(150, 1)



