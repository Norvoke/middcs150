import random

def maze():
    x = 0
    while x < 1000:
        a = random.randint(0,3)
        if a == 1:
            print("|",end='')
        elif a == 2:
            print("\\",end='')
        elif a == 3:
            print("/",end='')
        else:
            print("-",end='')
        x += 1