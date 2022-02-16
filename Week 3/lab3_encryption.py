"""
CS 150 Lab 3

Name: Finn Ellingwood

Creativity: I created the my_encrypt and my_decrypt
functions to encrypt and decrypt single words into
pig latin and back again.

"""

from random import randint, seed

ALPHABET = "abcdefghijklmnopqrstuvwxyz "
FOOLS_EXPANSION = 3

#---------------------------------------------------------
# Fools functions


# TODO: Write your fools function(s) here
def fools_encrypt(secret):
    """
    Encrypt message by multiplying each letter
    by a factor of FOOLS_EXPANSION
    Args:
        message: String to encrypt
    Return:
        encrypted message string
    """
    
    result = ''
    for c in secret:
        result += c*FOOLS_EXPANSION
    return result
    
def fools_decrypt(message):
    """
    Decrypt message that was encrypted using fools_encrypt.
    Args:
        message: String to decrypt
    Return:
        Decrypted message string
    """
    
    decrypted = ""
    for i in range(0, len(message), FOOLS_EXPANSION):
        decrypted += message[i]   
    return decrypted

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



def caesar_encrypt(message, shift):
    """
    Create an encryped message shifted by a number of letters
    
    Args:
        message: The message to be incrypted
        num: Integer amount to shift message in ALPHABET

    Returns:
        message shifted by num characters in ALPHABET
    """
    final_message = ''
    for i in range(len(message)):
        final_message = final_message + shift_letter(message[i], shift)
    return final_message
        

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
    spot = message.find(letter)
    first_half = message[:(spot)]
    second_half = message[(spot + 1):]
    return first_half + second_half


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
    
    


def subst_encrypt(msg, key):
    """
    Encrypts a message by using the key genrated by
    keygen and uses the jumbled around ALPHABET
    to reassign each letter
    
    Args:
        msg: Message to be encrypted.
        key" A string of the entire alphabet including ' '
        that will be used to reassign each letter.
    
    Returns:
        A message encrypted by reassigning each letter in
        the string msg with the given key
    """
    
    final_msg = ''
    for c in msg:
        index = ALPHABET.find(c)
        final_msg += (key[index])
    return final_msg

def subst_decrypt(msg, key):
    """
    Decrypts a message by using the key genrated by
    keygen and uses the unjumbled around ALPHABET
    to reassign each letter
    
    Args:
        msg: Message to be decrypted.
        key" A string of the entire alphabet including ' '
        that will be used to reassign each letter.
    
    Returns:
        A message decrypted by reassigning each letter in
        the string msg with the given key
    """
    
    final_msg = ''
    for c in msg:
        index = key.find(c)
        final_msg += (ALPHABET[index])
    return final_msg

def my_encrypt(msg):
    """
    Translates a word into pig latin
    
    example: translates 'hello' to 'ellohay'
    and 'dog' to 'ogday'
    
    Args:
        msg: A message to be translated into pig latin
        
    Returns:
        A message translated into pig latin
    
    """
    first = msg[0]
    
    final_msg = ''
    
    c = 1
    
    while c < len(msg):
        final_msg = final_msg + msg[c]
        c += 1
    final_msg = final_msg + first + 'ay'
    return final_msg

def my_decrypt(msg):
    """
    Translates a word from pig latin to English
    
    example: translates 'ellohay' to 'hello'
    and 'ogday' to 'dog'

    Args:
        msg: A message to be translated back into English
        
    Returns:
        A message translated back into English
    
    """
    first = msg[-3]
    
    final_msg = first
    
    c = 0
    
    while c < len(msg) - 3:
        final_msg = final_msg + msg[c]
        c += 1
    final_msg = final_msg
    return final_msg
        
    
    
    