# CS 150 recursion examples

import sys

def countdown(n):
    """
    Recursive function to count down from n to 1
    Args:
        n: integer >= 0
    Returns:
        None
    """
    if n > 0:
        print(n)
        countdown(n-1)
        
# countdown(5)

def factorial(n):
    """
    Recursive function to compute n! where n >= 0
    Args:
        n: integer >= 0
    Returns:
        n!
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
# factorial(5)
    
def reverse(s):
    """
    Recursive function to reverse string s
    Args:
        s: string to be reversed
    Returns:
        Reverse of string s
    """
    if len(s) == 0:
        return ''
    else:
        result = reverse(s[1:]) + s[0]
        return result
    
# reverse('abcdefg')
    
def palindrome(s):
    """
    Checks if string s is a palindrome
    Args:
        s: a string to be checked
    Returns:
        Boolean value of whether s is a palindrome
    """
    if len(s) <= 1:
        # base case -- an empty string or a single character is automatically a palindrome
        return True
    else:
        # recursive case -- a string is a palindrome if the first and last characters match and the rest of the string is a palindrome
        return (s[0]==s[-1]) and palindrome(s[1:-1])

# palindrome('racecar')
# palindrome('abcdefg')

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
