# CS 150 class example

"""
An example illustrating the use of the sys module
to get the command-line arguments (from sys.argv)
"""

import sys

if __name__ == "__main__":
    # Print the command-line arguments in list form
    print("Arguments: " + str(sys.argv))

    # Print out the command-line arguments, one at a time 
    # with the index
    for i in range(len(sys.argv)):
        print(str(i) + ": " + sys.argv[i])
