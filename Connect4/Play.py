#
# Playing the game    
#

from BoardClass import Board
from PlayerClass import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board
#Function 1
def process_move(player,board):
    #Ask about number in total or for the player itself
    #Connect four, printing an extra board in the end
    """takes two parameters: a Player object for the player whose move is being processed, and a Board object for the game that is being played
    """
    s = player.__repr__() + "\'s turn"
    print(s)
    column = player.next_move(board) #b
    player.num_moves += 0
    board.add_checker(player.checker,column)#c
    print()
    print(board)
    if board.is_win_for(player.checker) == True:
        print (player, "wins in", player.num_moves, "moves")
        print ("Congratulations!")
        return True
    elif board.is_full() :
        print ("It's a tie!")
        return True
    else:
        return False

    
#Function 2
#FIX
class RandomPlayer(Player):
    
    def next_move(self,board):
        """ choose at random from the columns in the specified board that are not yet full, and return the index of that randomly selected column. 
        """
        self.num_moves += 1
        ch = []
        for i in range(board.width):
            if board.can_add_to(i) == True:
                ch += [i]
        return random.choice(ch)
        
    
        
    
