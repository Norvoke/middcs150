"""
CSCI 150 Lab 6

Name: Finn Ellingwood
Section: B

Creativity: I implemented pretty win and loss screens with colored ascii art.
I also added a message that is given to the uses referencing an old computer
science joke if the word is terminal.


"""

import random as r

guessed_letters = set()

start_guesses = 0

win = """ \033[0;32m
▄██   ▄    ▄██████▄  ███    █▄        ▄█     █▄   ▄█  ███▄▄▄▄   
███   ██▄ ███    ███ ███    ███      ███     ███ ███  ███▀▀▀██▄ 
███▄▄▄███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███ 
▀▀▀▀▀▀███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███ 
▄██   ███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███ 
███   ███ ███    ███ ███    ███      ███     ███ ███  ███   ███ 
███   ███ ███    ███ ███    ███      ███ ▄█▄ ███ ███  ███   ███ 
 ▀█████▀   ▀██████▀  ████████▀        ▀███▀███▀  █▀    ▀█   █▀  
                                                                \033[0;0m
"""

loss = """ \033[0;31m
▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████  ▐██▌ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀  ▐██▌ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███    ▐██▌ 
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄  ▓██▒ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒ ▒▄▄  
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ░▀▀▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░  ░ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░       ░ 
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░ ░    
 ░ ░                                                                 \033[0;0m
"""



def play_wordgame(file, guesses):
    """
    Uses the read_words to pick a random word from the given
    file and creates an appropriate blank word with given
    number of blanks and then moves to word_prompt.
    
    Args:
        file: an existing txt file of words
        
        guesses: the max number of guesses the game is played with
        
    Returns:
        A list of words pulled from the txt file
    """
    word_list = read_words(file)
        
    start_guesses = guesses
        
    picked_word = word_list[r.randint(0, len(word_list))]
        
    blanks = ''
        
    for i in picked_word:
            blanks = blanks + '_'
    print("-----------------")
    word_prompt(blanks, picked_word, guesses)
    return
        
def word_prompt(blanks, picked_word, guesses):
    """
    Acts as the main function which prompts the user to
    enter a letter and checks if it works or not. Also awards
    the user if winner or loser and if guesses hav run out.
    
    Args:
        blanks: the given word with blank letters included
        
        picked_word: the given correct word
        
        guesses: the current number of guesses
        
    Returns:
        nothing
    """
    if picked_word == 'terminal':
        print("""\033[0;31m        ACHTUNG!\n
            ALLES TURISTEN UND NONTEKNISCHEN LOOKENSPEEPERS!\n
            DAS KOMPUTERMASCHINE IST NICHT FÜR DER GEFINGERPOKEN UND MITTENGRABEN! ODERWISE IST EASY TO SCHNAPPEN DER SPRINGENWERK, BLOWENFUSEN UND POPPENCORKEN MIT SPITZENSPARKEN.\n
            IST NICHT FÜR GEWERKEN BEI DUMMKOPFEN. DER RUBBERNECKEN SIGHTSEEREN KEEPEN DAS COTTONPICKEN HÄNDER IN DAS POCKETS MUSS.\n
            ZO RELAXEN UND WATSCHEN DER BLINKENLICHTEN.\033[0;0m\n
            """)
        return
    guessed_list = set_to_string(guessed_letters)
    print("Guessed letters: ", end='')
    for i in range(len(guessed_list)):
        print(guessed_list[i], end='')
    print('')
    print("Incorrect guesses left: ", end='')
    for i in range(guesses+1):
        print('*', end='')
    print('')
    print("Word:", blanks)
    letter = input('Guess a letter: ')
    alphabet = 'abcdefghijklmnoprstuvwxyz'
    if letter not in (alphabet + alphabet.upper()):
        word_prompt(blanks, picked_word, guesses)
    if len(letter) != 1:
        word_prompt(blanks, picked_word, guesses)
    if letter.upper() in guessed_list:
        print('Letter already guessed!')
        word_prompt(blanks, picked_word, guesses)
    guessed_letters.add(letter.upper())
    old_blanks = blanks
    blanks = insert_letter(letter, blanks, picked_word)
    if guesses == 0:
        print(loss)
        print('The word was:', picked_word)
        print("Better luck next time!")
        pass
    if blanks == old_blanks and (guesses != 0):
        print("-----------------")
        guesses = guesses - 1
        word_prompt(blanks, picked_word, guesses)
    if blanks == picked_word and (guesses != 0):
        print(win)
        print('The word was:', picked_word)
        print('You guessed it with ', end='')
        print(guesses - start_guesses, end='')
        print(' incorrect guesses')
        return
    if letter in picked_word and (guesses != 0):
        print("-----------------")
        word_prompt(blanks, picked_word, guesses)
            
def read_words(file):
    """
    Opens the given file and reads it into a list to be used later
    
    Args:
        file: an existing txt file
        
    Returns:
        A list of words pulled from the txt file
    """
    l = []
    
    with open(file, "r") as file:
        for line in file:
        # Assumes word entry per line
            l.append(line.strip())
    return l

def insert_letter(letter, blanks, full_word):
    """
    Adds the given letter to the word if appropriate
    
    Args:
        letter: given letter to be added
        
        blanks: the chosen word with unguessed blanks included
        
        full_word: the full chosen word
        
    Returns:
        the word with appropriate updated blanks
    """
    i = 0
    for element in range(0, len(full_word)):
        if full_word[element] == letter:
            blanks = blanks[:element] + letter + blanks[1 + element:]  
    return blanks


def set_to_string(iterable):
    """
    Converts a given set into a list of its constituent letters
    
    Args:
        iterable: an existing set of letters
        
    Returns:
        A list of capital letters
    """
    l = ''
    for item in iterable:
        l +=(str(item).upper()+' ')
    return l
    

if __name__ == '__main__':
    play_wordgame('cs_words.txt', 7)
