"""
CS150 class examples on files, lists
"""

def sentence_stats(sentence):
    """
    Print out various statistics about a sentence
    
    Args:
        sentence: string to be analyzed
    """
    words = sentence.split()
    print_stats(words)
    
def print_stats(words):
    """
    Print out various statistics about the input collection of strings
    
    Args:
        words: Collection of strings
    """
    print("Number of words: " + str(len(words)))
    if len(words) > 0:
        print("Longest word: " + longest_word(words))
        print("Shortest word: " + shortest_word(words))
        print("Avg. word length: " + str(average_word_length(words)))

# NOTE: if you want to try the examples from class you'll need to
# download the file of English words, "english.txt"

def file_stats(filename):
    """
    Print out various statistics about words in file.
    
    Assumes one word per line.
    
    Args:
        filename: Path to file
    """
    words = read_file(filename)
    print_stats(words)

def read_file(filename):
    """
    Read file into list of words assuming one word per line.

    Args:
        filename: Path to file
        
    Return:
        List of words
    """
    with open(filename, "r") as word_file:
        words = []
        
        for line in word_file:
            # Assumes one word per line 
            # (remember to strip newline from end of line)
            words.append(line.strip())    
        
        return words
    
def read_ints(filename):
    """
    Read file into list of integer assuming one integer per line.

    Args:
        filename: Path to file
        
    Return:
        List of integers
    """
    with open(filename, "r") as num_file:
        nums = []
        
        for line in num_file:
            # Assumes one word per line 
            # (remember to strip newline from end of line)
            nums.append(int(line.strip()))    
        
        return nums
    
def read_floats(filename):
    """
    Read file into list of integer assuming one integer per line.

    Args:
        filename: Path to file
        
    Return:
        List of integers
    """
    with open(filename, "r") as num_file:
        nums = []
        
        for line in num_file:
            # Assumes one word per line 
            # (remember to strip newline from end of line)
            nums.append(float(line.strip()))    
        
        return nums
    
def average_word_length(words):
    """
    Compute the average length of collection of strings.
    
    Args:
        words: Collection of strings
        
    Return:
        Float of average word length
    """
    length_sum = 0
    
    for word in words:
        length_sum += len(word)
    
    return length_sum / len(words)
        
def longest_word(words):
    """
    Find longest string in collection of strings.

    Args:
        words: Non-empty collection of strings
        
    Return:
        Longest string in words
    """
    longest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

def shortest_word(words):
    """
    Find shortest string in collection of strings.
    
    Args:
        words: Non-empty collection of strings
    
    Return:
        Shortest string in words
    """
    shortest = words[0]
    
    for word in words:
        if len(word) <  len(shortest):
            shortest = word
      
    return shortest
