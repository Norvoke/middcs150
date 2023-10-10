"""
CS150 list examples

Compute summary statistics "online" without lists
"""

def get_scores_and_print_stats():
    """
    Read user input of numerical scores, print average, min, max.
    """
    print("Enter the scores one at a time.  Blank score finishes.")
    
    line = input("Enter score: ")
    score = float(line)

    count = 0
    sum = 0
    smallest = score
    largest = score
    
    while line != '': 
        score = float(line)
        sum += score
        count += 1
        if score < smallest:
            smallest = score
        if score > largest:
            largest = score
            
        # Get next score from the user
        line = input("Enter score: ")
    
    # Print statistics

    average = sum / count
    
    print("-" * 10)
    
    print("Class max: " + str(largest))
    print("Class min: " + str(smallest))
    print("Class average: " + str(average))
    
# To run: 
# get_scores_and_print_stats()
