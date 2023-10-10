"""
CSCI 150 Test Project

Name: Finn Ellingwood
Section: B

Creativity: Implemented a simple naming system so that each player
is labeled with the name given when asked for X/O placement
and when they win. I also added a help screen when
the player inputs '?' as their answer to show the which
numbers correspond to which location on the game board.

"""

game_board = [' ',' ',' ', # Global variable as a list 9 as the empty board
              ' ',' ',' ',
              ' ',' ',' ']

board_reference = ("""     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     """+'\n') # Global variable defining the help board

game_won = False
game_tied = False
winner = 'A' # Global variable defining the winner, if none, just 'A' is used


def play_game():
    """
    The general function which prints the welcome text, prompts the players for
    their names used in winning messege and when asking for X/O placement.
    Begins the while loop which calls on the board generation and win
    checks to play game.
    
    Args: None
    
    Returns: Nothing
    """
    print("Welcome to Finn's Tic-Tac-Toe!\n")
    name1 = input("What is player X's name? ")
    name2 = input("What is player O's name? ")
    print("\nThe game board is labeled with each number corresponding")
    print("to and empty spot for a player to place an 'X' or an 'O'.\n")
    print(board_reference)
    print("Type and enter '?' at anytime to see this reference board.")
    while game_won == False and game_tied == False:
            check_if_tie()
            check_horiz_win(name1, name2)
            check_vert_win(name1, name2)
            check_dia_win(name1, name2)
            if game_tied or game_won:
                return
            move1 = player_move(name1)
            game_board[move1-1] = 'X'
            generate_board()
            check_if_tie()
            check_horiz_win(name1, name2)
            check_vert_win(name1, name2)
            check_dia_win(name1, name2)
            if game_tied or game_won:
                return
            move2 = player_move(name2)
            game_board[move2-1] = 'O'
            generate_board()
    
def generate_board():
    """
    Uses the global variable game_board to print the current state of the game
    
    Args: None
    
    Returns: Nothing
    """
    empty_line = "     |     |     "
    empty_horiz = "_____|_____|_____"
    print('\n'+empty_line)
    print("  "+game_board[0]+"  |  "+game_board[1]+"  |  "+game_board[2]+"  ")
    print(empty_horiz)
    print(empty_line)
    print("  "+game_board[3]+"  |  "+game_board[4]+"  |  "+game_board[5]+"  ")
    print(empty_horiz)
    print(empty_line)
    print("  "+game_board[6]+"  |  "+game_board[7]+"  |  "+game_board[8]+"  ")
    print(empty_line+'\n')
    
def player_move(player_name):
    """
    Prompts the user for a valid move and continues to ask until valid move is
    given.
    
    Args:
        player_name: The respective players name for asking their move
    
    Returns:
        int(move_choice): The valid location on the game board which
        the player chose to put their X/O
    """
    prompt = player_name+"'s move (choose from 1-9): "
    invalid_prompt = "Invalid move. Please choose from 1-9: "
    space_taken = "Space already taken. Choose another: "
    move_choice = input(prompt)
    while move_choice == "?":
        print(board_reference)
        move_choice = input(prompt)
    move_choice = int(move_choice)
    while move_choice not in range(1, 10):
        move_choice = int(input(invalid_prompt))
    while game_board[move_choice-1] != ' ':
        move_choice = int(input(space_taken))
    return int(move_choice)

def check_if_tie():
    """
    Checks if the game board is full and no more moves can be made to win the
    game
    
    Args: None
    
    Returns: Nothing
    """
    global game_tied
    if ' ' not in game_board:
        print("It's a tie! Everybody wins! Or nobody does...")
        game_tied = True

def check_horiz_win(name1, name2):
    """
    Checks the 3 horizontal rows to see if game is won and changes the states
    of the global variables 'winner' and 'game_won' respectively
    
    Args:
        name1: The name of the X player
        name2: The name of the O player
    
    Returns:
        bool: True if game is won, False if not
    """
    global winner
    global game_won
    if game_board[0] != ' ' and game_board[0] == game_board[1] == game_board[2]:
        winner = game_board[0]
        game_won = True
        win_message(name1, name2)
        return True
    if game_board[3] != ' ' and game_board[3] == game_board[4] == game_board[5]:
        winner = game_board[3]
        game_won = True
        win_message(name1, name2)
        return True
    if game_board[6] != ' ' and game_board[6] == game_board[7] == game_board[8]:
        winner = game_board[6]
        game_won = True
        win_message(name1, name2)
        return True
    else:
        return False

def check_vert_win(name1, name2):
    """
    Checks the 3 vertical columns to see if game is won and changes the states
    of the global variables 'winner' and 'game_won' respectively
    
    Args:
        name1: The name of the X player
        name2: The name of the O player
    
    Returns:
        bool: True if game is won, False if not
    """
    global winner
    global game_won
    if game_board[0] != ' ' and game_board[0] == game_board[3] == game_board[6]:
        winner = game_board[0]
        game_won = True
        win_message(name1, name2)
        return True
    if game_board[1] != ' ' and game_board[1] == game_board[4] == game_board[7]:
        winner = game_board[1]
        game_won = True
        win_message(name1, name2)
        return True
    if game_board[2] != ' ' and game_board[2] == game_board[5] == game_board[8]:
        winner = game_board[2]
        game_won = True
        win_message(name1, name2)
        return True
    else:
        return False
    
def check_dia_win(name1, name2):
    """
    Checks the 2 diagonal rows to see if game is won and changes the states
    of the global variables 'winner' and 'game_won' respectively
    
    Args:
        name1: The name of the X player
        name2: The name of the O player
    
    Returns:
        bool: True if game is won, False if not
    """
    global winner
    global game_won
    if game_board[0] != ' ' and game_board[0] == game_board[4] == game_board[8]:
        winner = game_board[0]
        game_won = True
        win_message(name1, name2)
        return True
    if game_board[2] != ' ' and game_board[2] == game_board[4] == game_board[6]:
        winner = game_board[1]
        game_won = True
        win_message(name1, name2)
        return True
    else:
        return False
    
def win_message(name1, name2):
    """
    Prints a win message given the winner global variable and the names of both
    players
    
    Args:
        name1: The name of the X player
        name2: The name of the O player
    
    Returns: Nothing
    """
    global winner
    if winner == 'X':
            print(name1+" wins! Good game!")
    if winner == 'O':
        print(name2+" wins! Good game!")
        
if __name__ == "__main__": # Starts the game if program is run with %Run
    play_game()