"""
CS 150 Lab 3

Name: 

Creativity: 

"""

from random import randint, seed

ALPHABET = "abcdefghijklmnopqrstuvwxyz "

#---------------------------------------------------------
# Fools functions

# TODO: Write your fools function(s) here


#---------------------------------------------------------
# Caesar's method

def shift_letter(letter, num):
    """
    Shift a letter by num places in ALPHABET with wraparound
    
    Args:
        letter: Character to shift
        num: Integer amount to shift character in ALPHABET

    Returns:
        letter shifted by num characters in ALPHABET
    """ 
    # Get the index of the current letter
    index = ALPHABET.find(letter)
    # We use the mod operator (%) for wraparound
    return ALPHABET[(index + num) % len(ALPHABET)]


# TODO: Write your caesar_encrypt function here


#---------------------------------------------------------
# Substitution cipher

def splice(message, letter):
    """
    Splice out letter from message and return remaining message

    For example:
    >>> splice("abcdefg", "f")
    'abcdeg'

    Args:
        message: String to remove letter from
        letter: Character that occurs exactly once in message
        
    Returns:
        message with letter removed

    """
    # TODO: fill in the details of this function


def keygen(password):
    """
    Generate a new random key using string password
    
    Args:
        password: String password used to generate key
    
    Returns:
        A key consisting of a random ordering of the letters in ALPHABET
    """
    remaining = ALPHABET
    key = ""
    
    seed(password)
    
    for _ in range(len(ALPHABET)):
        index = randint(0, len(remaining)-1)
        next_letter = remaining[index]
        key = key + next_letter
        remaining = splice(remaining, next_letter)
    
    return key
    
# TODO: Fill in your substitution functions here
