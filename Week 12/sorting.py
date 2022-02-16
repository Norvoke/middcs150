"""
CS 150 Sorting Examples
"""

import random
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#%%

def selection_sort(a_list):
    """
    Sort list in place using the selection sort algorithm

    Args:
        a_list : List to sort in place
    """
    # In each iteration, find the next smallest element in the list
    # and swap it into the appropriate place
    for i in range(len(a_list)):
        # Find the index of the smallest value from i onwards
        min_index = i
        min_value = a_list[i]        
        
        for j in range(i+1, len(a_list)):
            if a_list[j] < min_value:
                min_index = j
                min_value = a_list[j]
                
        # Swap i and min_index
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

#%%

#a = list(range(10))
#random.shuffle(a)

#a
#selection_sort(a)
#a

#%%

def insertion_sort(a_list):
    """
    Sort list in place using the insertion sort algorithm

    Args:
        a_list : List to sort in place
    """
    for i in range(1,len(a_list)):
        # Values at [0,i-1] are sorted already
        # Shift up all values in [0,i-1] greater than a_list[i]
        value = a_list[i]
        index = i
        
        while index > 0 and a_list[index-1] > value:
            a_list[index] = a_list[index-1]
            index -= 1
        # Now insert value (old a_list[i]) in its proper place
        a_list[index] = value
        # Now everything from 0...i is sorted

#%%
        
def merge_sort(a_list):
    """
    Sort list using the merge sort algorithm returning a new sorted list.

    Args:
        a_list: List to sort

    Returns:
        New sorted list
    """
    
    if len(a_list) <= 1:
        # Base case: List with single value is already sorted
        return a_list
    else:
        # Recursive case: Split list in half, sort each half then merge
        # the resulting lists                
        mid_index = len(a_list) // 2
        left  = merge_sort(a_list[:mid_index])
        right = merge_sort(a_list[mid_index:])
        #print("Left: ", left)
        #print("Right: ", right)        
        merged = merge(left, right)
        #print("Merged: ", merged)
        return merged

def merge(list1, list2):
    """
    Return a sorted list produced from merging two sorted lists

    Args:
        list1, list2: Sorted lists to merge

    Returns:
        Sorted, merged, list
    """
    result = []
    index1 = 0
    index2 = 0
    
    # Iterate each of the lists an item at a time
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            # If the current item in list1 is smaller, copy
            # and advance current item in list1
            result.append(list1[index1])
            index1 += 1
        else:
            # Otherwise, do the same in list2
            result.append(list2[index2])
            index2 += 1
    
    # Append any remaining elements in list1 or list2. Only one of these lists
    # should have any remaining elements, the other slicing operation
    # will produce an empty list
    result += list1[index1:]    
    result += list2[index2:]    
    
    return result


#%%

#a = list(range(8))
#random.shuffle(a)

#a
#merge_sort(a)

#%%

def time_sort(size, sort_function):
    """
    Invoke and time sort_function on random data of length size

    Args:
        size: Size of random test data to generate
        sort_function: Sorting function to invoke
    
    Returns:
        Time required to sort
    """
    # get some random data
    data = list(range(size))
    random.shuffle(data)
    
    start = time.time()
    sort_function(data)
    return time.time()-start

def compare_sorting():
    """
    Generate plot of runtime for selection sort, merge sort and built-in sort
    """
    sel = []
    mer = []
    blt = []

    sizes = range(500, 10000, 500);
    
    for size in sizes:
        sel.append(time_sort(size, selection_sort))
        mer.append(time_sort(size, merge_sort))
        blt.append(time_sort(size, sorted))
        print("N = %4d, select.: %4.2fs, merge: %4.3fs, sorted: %4.3fs" %
              (size, sel[-1], mer[-1], blt[-1]))
        
    plt.plot(sizes, sel, label="Selection")
    plt.plot(sizes, mer, label="Merge")
    plt.plot(sizes, blt, label="sorted built-in")
    plt.xlabel("List size")
    plt.ylabel("Sorting time in seconds")
    plt.title("Timing sorting algorithms")
    plt.legend(loc='upper left')
    plt.show()
    
#%%%

#compare_sorting()

#%%    
