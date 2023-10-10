"""
CS 150 complexity examples
"""

def mean(data):
    """
    Return mean of iterable data
    """
    return sum(data) / len(data)
    
def stddev(data):
    """
    Return standard deviation for iterable data
    """      
    result = 0.0
    average = mean(data)
    for d in data:
        result += (d - average) ** 2
    return math.sqrt(result / (len(data) - 1))
    
def stddev2(data):
    """
    Return standard deviation for iterable data
    """      
    result = 0.0
    for d in data:
        result += (d - mean(data)) ** 2
    return math.sqrt(result / (len(data) - 1))

def power(base, exp):
    """Compute base^exp using simple recursive definition"""
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)

def power(base, exp):
    """Compute base^exp using recursion, efficient version"""
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif exp % 2 == 0:
        sub = power(base, exp//2)
        return sub * sub
    else:
        return base * power(base, exp-1)
    

