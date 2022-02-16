# CS 150 class example
# Demonstrates writing a module

"""
Some basic functions to illustrate how modules work

A more detailed description of the module.
"""

# Constants/variables that will be used inside this module.
SOME_CONSTANT = 10

def a():
    """ Prints out the number 10 """
    print(SOME_CONSTANT)
    
def b(x, y):
    """ Returns x plus y """
    return x+y

def c(some_string):
    """ Returns the first and last character of some_string """
    return some_string[0] + some_string[-1]

print("This is line 25")

if __name__ == "__main__":
    print("Running the module", __name__)
else:
    print("Importing the module", __name__)
