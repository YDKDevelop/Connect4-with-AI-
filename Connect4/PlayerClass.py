#
# A Connect-Four Player class   
#

from BoardClass import Board

# write your class below

class Player :
    #Function 1
    def __init__ (self, checker) :
        """A new Player object with the two attributes: checker and num_moves
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    #Function 2
    def __repr__ (self) :
        """returns a string representing a Player object. The string returned should indicate which checker the Player object is using. 
        """
        s = "Player " + self.checker
        return s
    
    #Function 3
    def opponent_checker(self) :
        """returns a one-character string representing the checker of the Player object’s opponent
        """
        if self.checker == "X":
            return "O"
        else:
            return "X"
        
    #Function 4
    def next_move(self, board):
        """accepts a Board object as a parameter and returns the column where the player wants to make the next move
        """
        column = int(input('Enter a column:'))
        can = board.can_add_to(column)

        while can == False:
            print('Try again!')
            column = int(input('Enter a column:'))
            can = board.can_add_to(column)
        if can == True:
            self.num_moves += 1
        return column
         
         
            
        
