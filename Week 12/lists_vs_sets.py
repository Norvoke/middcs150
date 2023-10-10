# CS 150 class example
# Tests timing of sets vs. lists

import random
import time

def generate_set(set_size):
    """Return a set of random integers of the given size"""
    data = set()
        
    while len(data) < set_size:
        data.add(random.randint(0, set_size*10))
    
    return data

def generate_list(list_size):
    """Return a list of random integers of the given size"""
    data = []
    
    for i in range(list_size):
        data.append(random.randint(0, list_size*10))
    
    return data

def query_data(data, num_queries, largest):
    """
    Given a set or list 'data', perform 'num_queries' checks to
    see whether a random integer between 0 and 'largest' is
    contained in 'data'.

    Return the total time taken.
    """
    
    # We'll count them for fun, but won't do anything with the count
    count = 0 
    
    begin = time.time()
    
    for i in range(num_queries):
        # Just check to see if a random number is in there
        random_num = random.randint(0, largest)
        
        if random_num in data:
            count += 1
            
    return time.time() - begin

def speed_test(set_size, num_queries):
    """Print timing for creating and querying of lists and sets"""
    # Generate random list
    begin = time.time()
    list_data = generate_list(set_size)
    print("List creation took %f seconds" % (time.time()-begin))
    
    # Generate random set
    begin = time.time()
    set_data = generate_set(set_size)
    print("Set creation took %f seconds" % (time.time()-begin))
    
    print("--")
    
    # Time the list querying
    elapsed = query_data(list_data, num_queries, set_size*10)
    print("List querying took %f seconds" % elapsed)

    # Time the list querying
    elapsed = query_data(set_data, num_queries, set_size*10)
    print("Set querying took %f seconds" % elapsed)




def speed_data(num_queries, set_size_min, set_size_max, step_size):
    """
    Print a table of runtimes for querying lists and sets of
    different sizes.
    """
    print("size\tlist\tset")
    
    for set_size in range(set_size_min, set_size_max, step_size):
        # Generate random list
        list_data = generate_list(set_size)
    
        # Generate random set
        set_data = generate_set(set_size)
    
        # Time the list querying
        list_elapsed = query_data(list_data, num_queries, set_size*10)

        # Time the list querying
        set_elapsed = query_data(set_data, num_queries, set_size*10)
        
        print("%d\t%f\t%f" % (set_size, list_elapsed, set_elapsed))


#speed_test(100000, 1000)
#speed_data(1000, 10000, 100000, 5000)
