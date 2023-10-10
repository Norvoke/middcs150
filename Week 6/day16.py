"""
CS 150 Examples

| union {1,2} U {2,3} = {1,2,3} a.union(b)

& intersection {1,2} n {2,3} = {2} a.intersect(b)

- difference {1,2} - {2,3} = {1} a.difference(b)

^ symmetric difference {1,2} (-) {2,3} = {1,3} a.symmetric.difference(b)

in  element of 3 E {1,2,3} element in set

<= subset {1,2} ≤ {2,3,1} a.isssubset(b)

>= superset {1,3,2} ≥ {1} a.issuperset(b)
"""

def set_intersection(set1, set2):
    """
    Return intersection of sets set1 and set2
    """
    result = set()
    for element in set1:
        if element in set2:
            result.add(element)
    return result

def set_symmetric_difference(set1, set2):
    """
    Return symmetric difference of sets set1 and set2
    """
    result = set()
    for element in set1:
        if element not in set2:
            result.add(element)
    for element in set2:
        if element not in set1:
            result.add(element)
    return result