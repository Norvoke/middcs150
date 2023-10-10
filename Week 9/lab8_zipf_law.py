"""
Plots the occurence of words in a file given their frequency

CS 150 Section B

Name: Finn Ellingwood
"""

import string
import matplotlib
import sys

def read_corpus(file_name):
    """
    Opens a text file provided and converts it to a list containing
    every given words in the file.
    
    Args:
        file_name: name of the given file.
        
    Returns:
        word_list: a list containing every given words in the file.
    """
    line_list = []
    word_list = []
    chars_to_remove = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    
    with open(file_name, "r") as file:
        for line in file:
            line_list.append(line.strip())
    for entry in line_list:
        line_words = entry.split()
        for word in line_words:
            word = word.strip(chars_to_remove)
            word_list.append(word.lower())
    
    return word_list

def count_and_rank(words):
    """
    Takes a given list of words and converts them to a tuple
    which gives each word a corresponding ranks.
    
    Args:
        word_list: name of the given list to be converted.
        
    Returns:
        word_count: a tuple containing a list of words and
        a list of counts for those words both sorted.
    """
    
    # Initialising a bunch of place holder lists, an empty dict, and the set of the words
    # with no duplicates.
    word_dict = {}
    word_set = set(words)
    word_list = []
    count_list = []
    sorted_words = []
    sorted_nums = []
    
    for word in word_set:
        count = words.count(word)
        word_dict[word] = count
        word_list.append(word)
        count_list.append(count)
    
    dict_list = [(word,count) for word,count in word_dict.items()]
    
    # Takes the dict of words with given rank and using the lambda variable
    # as the key, it sorts them and adds them to a part list in descending order.
    sorted_list = sorted(dict_list, key=lambda t : t[1], reverse=True)
    
    for word,count in sorted_list:
        sorted_words.append(word)
        sorted_nums.append(count)
        
    sorted_tup = sorted_words, sorted_nums
    
    return sorted_tup

def print_top_ten(sorted_tup):
    """
    Prints the top 10 words with the most occurences in the given tuple
    
    Args:
        sorted_tup: the already sorted tuple containin the words and
        given rank in descending order.
        
    Returns:
        Nothing
    """
    word_list = sorted_tup[0]
    rank_list = sorted_tup[1]
    
    print("WORD"+"\t"+"RANK")
    
    # If there are less then 10 entrys in the tuple it prints the existing ones
    if len(word_list) < 10:
        for i in range(len(word_list)):
            print(word_list[i], end="\t")
            print(rank_list[i])
            i+=1
    # Else it just prints the top 10 if > 10
    else:
        for i in range(10):
            print(word_list[i], end="\t")
            print(rank_list[i])
            i+=1
        
if __name__ == "__main__":
    """
    Prints the top 10 most used words from the command-line-given text file
    """
    if len(sys.argv) != 2:
        pass
    else:
        print_top_ten(count_and_rank(read_corpus(sys.argv[1])))
