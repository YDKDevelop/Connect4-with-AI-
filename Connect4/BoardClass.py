#
# A Connect Four Board Class
#

class Board:
#Funtion 1 
    def __init__ (self, height, width) :
        """ the constructor that constructs a new BOARD object """
        self.width = width
        self.height = height
        self.slots = [[' ']*self.width for row in range(self.height)]
#Function 2
    def __repr__(self):
        """returns a string representing a Board object"""
        s = ''   
        for row in range(self.height):
            s += '|'   
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += (2*self.width +1) * '-'    
        s += '\n'
        for col in range(self.width):
            s += " " + str(col % 10)
        
        return s
#Function 3
    def add_checker(self, checker, col):
        """Method that accepts two inputs: checker and col
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        row = 0
        while row + 1 < self.height:
            if self.slots[row+1][col]==' ':
                row += 1
            else:
                break
        self.slots[row][col] = checker
        
        
#Function 4
    def reset(self):
        """Reset the Board object on which it is called by setting all slots to contain a space character"""
        self.slots = [[' '] *self.width for row in range(self.height)]

#Function 5
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker,col)
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

#Function 6
    def can_add_to(self,col):
        """Returns True if it is valid to place a checker in the column col on the calling Board object. Otherwise, it should return False
        """
        if col < 0:
            return False
        elif col >= self.width:
            return False
        elif self.slots[0][col] != ' ' :
            return False
        else:
            return True
#Function 7
    def is_full(self):
        """returns True if the called Board object is completely full of checkers, and returns False otherwise
        """
        for i in self.slots[0] :
                if i == ' ' :
                    return False
        return True

#Function 8
    def remove_checker(self,col):
        """removes the top checker from column col of the called Board object. If the column is empty, then the method should do nothing.
        """
        for i in range (self.height) :
            if self.slots[i][col] != ' ':
                self.slots[i][col] = ' '
                return

#Function 9
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
         """ Checks for vertical win
         """
         for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

         return False

    def is_down_diagonal_win(self, checker):
         """Checks for down diagonal win
         """
         for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

         return False

    def is_up_diagonal_win(self, checker):
         """Checks for up diagonal win
         """
         for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col + 3] == checker and \
                   self.slots[row + 1][col + 2] == checker and \
                   self.slots[row + 2][col + 1] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

         return False

    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 'O', and returns True if there are four consecutive slots containing checker on the board. Otherwise, it should return False.
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) or \
           self.is_vertical_win(checker) or \
           self.is_down_diagonal_win(checker) or \
           self.is_up_diagonal_win(checker):
            return True
        
        return False
