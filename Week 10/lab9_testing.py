import turtle as t

def sierpinski(length, generation):
    if generation == 0:
        t.forward(length)
    else:
        for _ in range(3):
            sierpinski(length/2, generation-1)
            t.left(60)
        