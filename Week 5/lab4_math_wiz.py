"""
CSCI 150 Lab 4

Name: Finn Ellingwood

Creativity: I added three difficulty levels, easy, normal, and hard,
which return equations one, two, and three operators respectively.
I added an easter egg where if the user gives an answer of 42 and
it is not correct, it will print a surpise message and continue asking
for the correct answer.

"""
import random as r
import time

start = 0 #Makes sure the start of the time interval is zero

def random_equation(numops):
    """
    Generates a random equation with a length determined
    by the number of operators given by the numops variable.
    
    Args:
        numops: the number of operators given as an integer.
        
    Returns:
        a string containing the finished equation containing
        the given number of operators.
    """
    equation = ''
    c = 0
    mult = "*"
    add = "+"
    sub = "-"
    i = 0
    numops += 1
    while c < numops:
        c += 1
        equation += str(r.randint(1,10))
        if c < numops:
            equation += r.choice([mult, add, sub])
    return equation

def query_equation(eqn):
    """
    Calls upon the random_equation function to generate a question
    with a correct answer and evaluates whether a given answer
    from the user is correct.
    
    Args:
        eqn: a list of numbers seperated by operators that pythan can evaluate.
    
    Returns:
        Nothing
    """
    start = time.time()
    guess = int(input(eqn + ' = '))
    answer = eval(eqn)
#     if guess == answer:
#         print("Correct!")
#         return
#     if abs(answer - guess) < 3:
#         print("Close. Try again.")
#         query_equation(eqn)
#     if guess == 42 and guess != answer:
#         print("While it is the answer to the great question ", end = '')
#         print("of the universe, it is not the correct answer to "+eqn+".")
#         print("Keep Trying.")
#         query_equation(eqn)
#     else:
#         print("Keep Trying.")
#         query_equation(eqn)
    if guess == answer:
        print("Correct!")
        return
    if guess == 42 and guess != answer:
        print("While it is the answer to the great question ", end = '')
        print("of the universe, it is not the correct answer to "+eqn+".")
        print("Keep Trying.")
        query_equation(eqn)
    elif abs(answer - guess) < 3:
        print("Close. Try again.")
        query_equation(eqn)
    else:
        print("Keep Trying.")
        query_equation(eqn)
        
def play_game(duration, ops):
    """
    Calls on the query_equation function to generate each question and determine if true.
    Ends the game once the time is elapsed and the final correct answer is given.
    
    Args:
        duration: Amount of time in seconds the game will elapse.
        ops: Number of operators each question will have.
    
    Returns:
        Nothing
    """
    score = 0
    start_time = time.time()
    while duration > time.time() - start_time:
        eqn = random_equation(ops)
        query_equation(eqn)
        score += 1
    endtime = str(time.time() - start_time)
    print("You got "+str(score)+" correct in "+endtime+" seconds.")
    
def main():
    """
    Launches the math wiz game by asking user if they want to play.
    If yes, asks for how long, how difficult, and plays until time is elapsed.
    If no, tells the user a goodbye message and returns nothing.
    """
    game_state = input("Do you want to play a game [yes/no]? ")
    if game_state == 'no':
        print("\033[1;32mHave a nice day, goodbye!")
        return
    if game_state == 'yes':
        duration = int(input("How long do you want to play for [seconds]? "))
        easy = "\033[3;32measy\033[0;0m"
        normal = "\033[3;33mnormal\033[0;0m"
        hard = "\033[3;31mhard\033[0;0m"
        difficulty = input("How difficult would you like the questions ["+easy+'/'+normal+'/'+hard+"]? ")
        if difficulty == 'easy':
            play_game(duration, 1)
        if difficulty == 'normal':
            play_game(duration, 2)
        if difficulty == 'hard':
            play_game(duration, 3)
            
if __name__ == '__main__':
    main()
