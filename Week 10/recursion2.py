"""
CS 150 recursion examples with pending operations
"""

def mystery(s):
    """
    Recursive function that takes string s as input and returns...
    """
    if s == '':
        return 0
    else:
        return int(s[0]) + mystery(s[1:])

# What output does this call produce?
# mystery('1337')


# go_back illustrates pending operations after the recursive call
def go_back(n):
    """
    Prints "Go" for each recursive call; "Stop" at base case;
    then prints "Back" on the way out of the recursion.
    Args:
        n: number of times to make recursive call
    """
    if n == 0:
        print("Stop")
    else:
        print("Go", n)
        go_back(n-1)
        print("Back", n)
        
# What output does this call produce?
# go_back(3)

        
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# factorial(5000)

# import sys
# sys.setrecursionlimit(10000)
# factorial(5000)



