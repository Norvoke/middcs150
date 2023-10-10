"""
CS 150 Examples
"""

# Constants
REPEAT = 2

def transform(s):
    result = ''
    for c in s:
        result += c*REPEAT
    return result

# BOOLEANS

t = True
f = False

# Relational operators <, <=, >, >=, ==, !=

# Boolean operators and, or, not

def is_odd(n):
    return n%2 == 1

def is_small_odd(n):
    return (n % 2 == 1) and (n < 10)

# IF-statements aka conditionals
"""
statement0
if condition 1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement4
statement4
    

n = int(input("Enter a number: "))
if n < 10:
    print("less than 10")
elif n < 20:
    print("less than 20")
elif n < 30:
    print("less than 30")
else:
    print("greater or equal to 30")

"""

def sign_of(n):
    print("checking the sign")
    if n > 0:
        print("input is positive") # statement 1
    elif n < 0:
        print("input is negative") # statement 2
    else:
        print("input is zero") # statement 3
    print("thank you for playing!") # statement 4