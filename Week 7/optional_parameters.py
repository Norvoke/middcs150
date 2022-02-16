# CS 150 class example

# Demonstrates optional parameters

def my_range_with_step(start, stop, step):
    """
    Return a range
    
    Args:
        start: inclusive start index
        stop: exclusive stop index
        step: range increment

    Returns: A list of integers
    """
    i = start
    r = []
    
    while i < stop:
        r.append(i)
        i += step
    
    return r

def my_range_with_unitstep(start, stop):
    return my_range_with_step(start, stop, 1)


def my_range(start, stop, step=1):
    """
    Return a range
    
    Args:
        start: inclusive start index
        stop: exclusive stop index
        step: range increment

    Returns: A list of integers
    """
    i = start
    r = []
    
    while i < stop:
        r.append(i)
        i += step
    
    return r
