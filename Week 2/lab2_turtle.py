"""
CS 150
F Ellingwood
Section B
Creativity:
1. Used the polygon function to create the explosion from the deathstar.
2. Used the triangle function to make ships fleeing from the planet.
3. Used multiple for loops and randomness to create star field, explosion,
and fleeing ships.
4. Used special draw_circle function to shade planets and detail the
star destroyer, as well as the death star.
5. The bulk of the volume of the code is due to the goto commands which
specified the certain location of the edges of a drawing. This could
possibly be compacted if the x,y pairs could be stored as a seperate
array or some other ordered list and accessed through a loop of
some
"""

import turtle as t
import random as r

#Triangle function used to draw the far away spaceships
def triangle(x, y, sidelen):
    t.pu()
    t.goto(x, y)
    t.pd()
    for _ in range(3):
        t.forward(sidelen)
        t.left(120)

#A General use function to draw a polygon of an size and color
# with numsides number of sides
def polygon(x, y, numsides, sidelen, color):
    angle = 360 / numsides
    jumpto(x, y)
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(numsides):
        t.forward(sidelen)
        t.right(angle)
    t.end_fill()

#A useful travel function that includes penup
def jumpto(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.right(60)

#A general function used to make circles of any size and color
def draw_circle(size, color):
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    
#Uses the draw_circle function to draw the 2 shaded planets
def add_planets():
    t.penup()
    t.pensize(5)
    t.pencolor("#242740")
    polygon(170, 200, 1000, 1.2, "#242740")
    t.goto(0, 0)
    jumpto(300, 350)
    draw_circle(300, "#949494")
    draw_circle(290, "#6b6b6b")
    draw_circle(280, "#4f4f4f")
    draw_circle(270, "#2b2b2b")
    draw_circle(260, "black")
    jumpto(450, 380)
    draw_circle(50, "#80abd1")
    t.goto(452, 385)
    draw_circle(44, "black")

#Draws the stars in the background
def add_circles(radius):
    for _ in range(500):
        x = r.randint(-600, 600)
        y = r.randint(-600, 600)
        t.penup
        jumpto(x, y)
        t.pensize(3)
        t.pencolor(r.uniform(0.8,1), r.uniform(0.8,1), r.uniform(0.8,1))
        t.pendown
        t.fillcolor("#9bb8e0")
        t.begin_fill()
        t.circle(radius)
        t.end_fill

#Draws the star destroyer from back to front
def star_destroyer():
    t.penup()
    jumpto(0, 0)
    draw_circle(44, "black")
    t.pd()
    t.begin_fill()
    t.color("black")
    t.goto(-570, -90)
    t.goto(-90, -470)
    t.goto(-30, -420)
    t.end_fill()
    t.goto(-300, 90)
    t.penup()
    t.goto(30, -440)
    t.goto(-30, -420)
    t.pd()
    t.begin_fill()
    t.goto(30, -440)
    t.goto(30, -400)
    t.goto(-30, -380)
    t.end_fill()
    t.pu()
    t.goto(0,0)
    t.pd()
    t.color("gray")
    t.begin_fill()
    t.color("gray")
    t.goto(30, -400)
    t.goto(-30, -380)
    t.goto(-300, 50)
    t.goto(0, 0)
    t.end_fill()
    t.goto(-300, 50)
    t.color("#383838")
    t.begin_fill()
    t.goto(-570, -50)
    t.goto(-90, -430)
    t.goto(-30, -380)
    t.goto(-300, 50)
    t.end_fill()
    t.pensize(50)
    t.goto(-300,100)
    t.goto(-380,70)
    t.goto(-300,100)
    t.color("gray")
    t.goto(-230,90)
    t.pensize(20)
    t.goto(-280,100)
    t.goto(-280,40)
    t.penup()
    t.goto(-270,110)
    draw_circle(20, "gray")
    t.goto(-350,100)
    draw_circle(20, "#383838")
    t.goto(-34, -50)
    draw_circle(20, "#666666")
    t.goto(-35, -150)
    draw_circle(21, "#666666")
    t.goto(-35, -250)
    draw_circle(22, "#666666")
    t.goto(-35, -350)
    draw_circle(22, "#666666")
    t.goto(-470, -80)
    draw_circle(20, "#262626")
    t.goto(-350, -170)
    draw_circle(20, "#262626")
    t.goto(-220, -270)
    draw_circle(20, "#262626")
    t.goto(-90, -360)
    draw_circle(20, "#262626")

#Draws the death star and laser explosion
def death_star():
    t.goto(-550, 300)
    draw_circle(100, "gray")
    t.goto(-540, 310)
    draw_circle(90, "#666666")
    t.goto(-450, 400)
    t.pensize(4)
    t.pd()
    t.color("gray")
    t.goto(-670, 400)
    t.pu()
    t.goto(-500, 410)
    draw_circle(30, "#444444")
    t.pencolor("#85ff87")
    t.pd()
    t.goto(-450, 440)
    t.pu()
    t.goto(-500, 470)
    t.pd()
    t.goto(-450, 440)
    t.goto(-530, 440)
    t.goto(-450, 440)
    t.goto(-260, 250)
    for _ in range(30):
        randdiff = r.randint(-10, 90)
        red = (r.randint(10, 80)/100)
        t.pencolor(red, 0, 0)
        polygon(randdiff + (-300), randdiff + 260, r.randint(5, 10), r.randint(10, 30), (red, 0, 0))

#Final image generator adding up all of the above
#element functions
def generate_picture():
    # hexagon(150)
    t.screensize(650,500)
    t.tracer(False)
    t.bgcolor("#242740")
    add_circles(r.uniform(0.1, 1.5))
    add_planets()
    star_destroyer()
    death_star()
    t.right(90)
    for _ in range(15):
        t.color("gray")
        t.begin_fill()
        triangle(r.randint(30, 500), r.randint(30, 500), r.randint(3, 30))
        t.end_fill()
    t.done()
