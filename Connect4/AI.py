#
# AI Player for use in Connect Four   
#

import random  
from Play import *

class AIPlayer(Player):
    #Funtion 2
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    #Function 3
    def __repr__(self):
        """returns a string representing an AIPlayer object
        """
        a = "Player " + self.checker
        a += " (" + self.tiebreak + ", " + str(self.lookahead)+")"
        return a

    #Function 4
    def max_score_column(self, scores):
        """ returns the index of the column with the maximum score
        """
        s = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                s += [i]
        if self.tiebreak == "LEFT":
            return s[0]
        elif self.tiebreak == "RIGHT":
            return s[-1]
        else:                               #for RANDOM
            return random.choice(s)
    
    #Function 5
    def scores_for(self,board):
        #Fix 
        """takes a Board object board and determines the called AIPlayer‘s scores for the columns in board.
        """
        scores = [50] * board.width
        for i in range(board.width):
            if  board.is_full():
                scores[i] = -1
            elif board.is_win_for(self.checker):
                scores[i] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                board.add_checker(self.checker,i)
                AI = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead - 1)
                opp_score = (AI.scores_for(board))
                scores[i] = 100 - max(opp_score)
                board.remove_checker(i)
        return scores
    
    

    #Function 6
    def next_move(self,board):
        """overrides (i.e., replaces) the next_move method that is inherited from Player.
        """
        self.num_moves += 1
        return self.max_score_column(self.scores_for(board))
    
        
                
                
            
            
        
        
    
