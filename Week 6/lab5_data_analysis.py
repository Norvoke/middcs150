"""
CSCI 150 Lab 5

Name: Finn Ellingwood

Creativity: I included a very simple mode function that is really only one line
with help from Maja and the online python documentation. I also tried to implement a way
of displaying where the middle 50 percent of the data is located by calculating the
first and third interquartile ranges and setting them as the opening and
closin of the 68% interval.

Enter file to analyze: 95age.txt
File contained 35326 entries
Max: 90
Min: 0
Average: 35.73141595425466
Median: 34.0
Std. dev: 22.54500613160593
Mode: 34
68% of the data occurs within the interval 13.186409822648727 to 58.27642208586059

This middle 68% likely makes sense with how we understand the distrobution of age in
human population. Also the min of 0 is reporting individuals born in 1995, ie age of 0.

Enter file to analyze: 95income.txt
File contained 35326 entries
Max: 304998
Min: -13411
Average: 16974.277925607203
Median: 8929.5
Std. dev: 22838.78036356643
Mode: 0
68% of the data occur within the interval -5864.502437959229 to 39813.058289173634

In this case the negative min results from individuals reporting a loss to the IRS.

Enter file to analyze: 95kids.txt
File contained 35326 entries
Max: 9
Min: 0
Average: 0.43285398856366414
Median: 0.0
Std. dev: 0.8975902261264251
Mode: 0
68% of the data occur within the interval -0.464736237562761 to 1.3304442146900892

In this case the middle 68% makes little sense because one can't have negative children.

"""

import os.path

mode = 0

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
    l = open_file(file) # Saves the list data from file as a list named l
    element_num = len(l)
    if os.stat(file).st_size == 0:
        print("File contained 0 entries")
    else:
        print("File contained "+str(element_num)+" entries")
        maxi = max(l)
        mini = min(l)
        total = sum(l)
        avg = total / element_num
        median = middle(l)
        dev = stdev(l)
        moded = mode(l)
        
        # Calculates the first and third quartile ranges
        Q1 = avg + dev
        Q3 = avg - dev
    
        print("Max:",maxi)
        print("Min:",mini)
        print("Average:",avg)
        print("Median:",median)
        print("Std. dev:",dev)
        print("Mode:", moded)
        print("68% of the data occur within the interval",Q3,"to",Q1)

def open_file(file):
    """
    Opens the given file and reads it into a list to be used later
    
    Args:
        file: an existing txt file
        
    Returns:
        A list of integers pulled from the txt file
    """
    l = []
    
    with open(file, "r") as file:
        for line in file:
        # Assumes one entry per line
            l.append(int(line.strip()))
    return l
            
def middle(l):
    """
    Calculates the standard deviation of a given list of integers
    
    Args:
        list: a list of integers in any order to be sorted
        
    Returns:
        The median of the given list either as an integer if the
        list is odd or average between the two middle values if the list
        is even
    """
    sorted_list = sorted(l)
    list_length = len(sorted(l))
    
    if len(sorted_list) % 2 == 1:
        midd = list_length // 2
        midd = sorted_list[midd]
    else:
        midd = list_length // 2
        midd = (sorted_list[midd] + sorted_list[midd - 1]) / 2
    return midd

def stdev(l):
    """
    Calculates the standard deviation of a given list
    
    Args:
        list: a list of integers in any order
        
    Returns:
        The standard deviation of the given list as a float
    """
    n = len(l)
    mean = sum(l) / n
    variance = sum((x - mean) ** 2 for x in l) / (n - 1)
    std_dev = variance ** .5
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
    
    # Had to hard code the final entry to be included because the for loop ends early
    print(str(previous) + "\t" + str(count))
    
def mode(data):
    
    """
    Attempts to return the mode of the list data
    
    Args:
        data: List of "sortable" data items
    
    Returns:
        the mode of a given list in data
    """
    # This appears to be the easiest way to calculate the mode according to the official python documentation
    mode = (max(set(data), key = data.count))
    
    return mode

if __name__ == '__main__':
    # This invokes the data_analysis function when the program is run
    if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()
    else:
        zip = sys.argv[3]
        file_name = sys.argv[2]
        get_temperature(zip)
    data_analysis()
