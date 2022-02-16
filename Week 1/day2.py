"""
CS 150 Example function definitions
2/16/2022
"""

def square(x):
    """
    Compute the square of a number
    
    Args:
        x: A number to be squared
    
    Returns:
        The value of the parameter squared
    """
    return (x**2)

def g(x):
    return 3*x

def average(a, b):
    sum = a + b
    return sum/2

# Try runnning these functions from the shell
def divide2_float(x):
    return x/2

def divide2_int(x):
    return x//2

def func(name, age):
    print(name, "is my name")
    print(age, "is my age")
    
def compound_interest(principal, rate, years):
    """
    Calculate the investment value compounded yearly
    
    Args:
        Principal: The amount of dollars to invest
        rate: Interest rate as a percentage (0.0, 1]
        years Number of years to compound interest
        
    Returns:
        Total value of investment after compounding interest over years
    """
    amount = principal * ((1+rate)**years)
    return amount