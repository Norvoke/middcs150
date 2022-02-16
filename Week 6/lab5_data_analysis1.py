"""
CSCI 150 Lab 5

Name: Finn Ellingwood

Creativity: 

Enter file to analyze: 95age.txt
File contained 35326 entries
Max: 90
Min: 0 (anyone who was born in 1995 would be 0)
Average: 35.73141595425466
Median: 34.0
Std. dev: 22.54500613160593

Enter file to analyze: 95income.txt
File contained 35326 entries
Max: 304998
Min: -13411 (this would represent a loss of money)
Average: 16974.277925607203
Median: 8929.5
Std. dev: 22838.78036356643

Enter file to analyze: 95kids.txt
File contained 35326 entries
Max: 9 (a lot of kids!)
Min: 0
Average: 0.43285398856366414
Median: 0.0
Std. dev: 0.8975902261264251
"""

import os.path

list = []

def data_analysis():
    """
    Asks the user to input an existing txt file to be read into
    a list and uses said list to calculate given statistics about it such
    as max, min, median, average, and standard deviation.
    
    Args:
        None
        
    Returns:
        Nothing
    """
    
    file = input("Enter file to analyze: ")
    
    if open_file(file):
        return
    
    # Work with file object
    # File is automatically closed when you exit the with block
    element_num = len(list)
    
    if len(list) == 0:
        print("File contained 0 entries")
    else:
        print("File contained "+str(element_num)+" entries")
        maxi = max(list)
        mini = min(list)
        total = sum(list)
        avg = total / element_num
        median = middle(list)
        dev = stdev(list)
    
        print("Max:",maxi)
        print("Min:",mini)
        print("Average:",avg)
        print("Median:",median)
        print("Std. dev:",dev)
    
    
def open_file(file):
    """
    Opens the given file and reads it into a list to be used later
    
    Args:
        file: an existing txt file
        
    Returns:
        A list of integers pulled from the txt file
    """
    if os.path.exists(file):
        with open(file, "r") as file:
            for line in file:
            # Assumes one entry per line 
            # (remember to strip newline from end of line)
                list.append(int(line))
    else:
        print("\033[3;31mERROR LOCATING SPECIFIED FILE!\033[0;0m")
        return True
    
def middle(list):
    """
    Calculates the standard deviation of a given list of integers
    
    Args:
        list: a list of integers in any order to be sorted
        
    Returns:
        The median of the given list either as an integer if the
        list is odd or average between the two middle values if the list
        is even
    """
    sorted_list = sorted(list)
    
    if len(sorted_list) % 2 == 1:
        midd = int(len(sorted_list) // 2)
        midd = sorted_list[midd]
    else:
        midd = int(len(sorted_list) // 2)
        midd = (sorted_list[midd] + sorted_list[midd - 1]) / 2
    return midd

def stdev(list):
    """
    Calculates the standard deviation of a given list
    
    Args:
        list: a list of integers in any order
        
    Returns:
        The standard deviation of the given list as a float
    """
    n = len(list)
    mean = sum(list) / n
    var = sum((x - mean) ** 2 for x in list) / (n - 1)
    std_dev = var ** .5
    return std_dev

def frequencies(data):
    
    """
    Attempts to print the frequency of each item in the list data
    
    Args:
        data: List of "sortable" data items
    """
    data.sort()
    
    count = 0
    previous = data[0]

    print("data\tfrequency") # '\t' is the TAB character

    for d in data:
        if d == previous:
            # Same as the previous, increment the count for the run
            count += 1
        else:
            # We've found a different item so print out the old and reset the count
            print(str(previous) + "\t" + str(count))
            count = 1
        
        previous = d
    print(str(data[-1]) + "\t" + "1")
        
# Main program that gets executed when program is run
# (Leave this as is, no changes to be made)
if __name__ == '__main__':
    # This invokes the data_analysis function when the program is run
    data_analysis()
