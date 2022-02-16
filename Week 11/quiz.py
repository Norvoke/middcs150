import turtle as t
def mystery(x):
    if x >= 10:
        t.dot(5)
        t.forward(x)
        t.left(90)
        t.forward(x/2)
        t.left(90)
        mystery(x/2)