"""
CS150 list examples

A set of functions for reading in scores and calculating
various statistics from the input scores.
"""

def get_scores():
    """
    Read user input of numerical scores as floats into a list.
    
    Return:    
        List of scores
    """
    print("Enter the scores one at a time.  Blank score finishes.")
    
    scores = []
    line = input("Enter score: ")
    
    while line != '':
        scores.append(float(line))
        line = input("Enter score: ")
    
    return scores
        
def manual_average(scores):
    """
    Calculate the average of the values in list scores.
    
    Args:
        scores: List of numeric scores
    
    Return:
        Average of scores as a float
    """
    
    # Compute "manually" without using built-in functions
    sum = 0
    count = 0
    
    for score in scores:
        sum += score
        count += 1
    
    return sum / count

def average(scores):
    """
    Compute average of list of scores.
    
    Args:
        scores: List of numeric scores
    
    Return:
        Average of scores as a float
    """
    return sum(scores) / len(scores)

def assign_grades(scores):
    """
    Calculate a letter grade for each numeric score in list.
    
    If a score is greater than or equal to the average
    then it receives an A. If it is less, an F.  

    Args:
        scores: List of numeric scores
        
    Return:
        List of letter grades assigned for each numeric score
        in corresponding order
    """
    avg = average(scores)
    grades = []
    
    for score in scores:
        if score >= avg:
            grades.append("A")
        else:
            grades.append("F")
    
    return grades

def print_class_stats(scores):
    """
    Print out various stats about the list of scores.

    Args:
        scores: List of numeric scores
    """
    print("Class max: " + str(max(scores)))
    print("Class min: " + str(min(scores)))
    print("Class average: " + str(average(scores)))
    print("Class grades:")
    
    grades = assign_grades(scores)
    
    for i in range(len(grades)):
        print(str(scores[i]) + " -> " + grades[i])

    
def main():
    """
    Get the scores from the user and then print out the stats.
    """
    scores = get_scores()
    print("-" * 10)
    print_class_stats(scores)
    
