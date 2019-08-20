#
#
# AI Player for use in Connect Four   
#

import random  
from randomPlayer import *

class AIPlayer(Player):
    """subclass of Player"""
    def __init__(self, checker, tiebreak, lookahead):
        """initializes AIPlayer class"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak.upper()
        self.lookahead = lookahead

    def __repr__(self):
        """returns string representing an AIPlayer object
        overrides one inherited from Player"""
        return "Player " + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """takes a list scores of each column and returns the index of the
        column with the ma score, if tied, use method for tiebreaking"""
        max_score = max(scores)
        ind_list = []
        for x in range(len(scores)):
            if max_score == scores[x]:
                ind_list += [x]
        if self.tiebreak == 'LEFT':
            return ind_list[0]
        elif self.tiebreak == 'RIGHT':
            return ind_list[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(ind_list)

    def scores_for(self, board):
        """takes Board object and determines the scores for each column"""
        scores = ['x']*board.width
        for x in range(board.width):
            if board.can_add_to(x) == False:
                scores[x] = -1
            elif board.is_win_for(self.checker):
                scores[x] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[x] = 0
            elif self.lookahead == 0:
                scores[x] = 50
            else:
                board.add_checker(self.checker, x)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead)-1)
                opp = opponent.scores_for(board)
                if max(opp) == 0:
                    scores[x] = 100
                elif max(opp) == 100:
                    scores[x] = 0
                else:
                    scores[x] = 50
                board.remove_checker(x)
        return scores

    def next_move(self, board):
        """overrides inherited method; returns best possible move"""
        col_scores = self.scores_for(board)
        self.num_moves += 1
        return self.max_score_column(col_scores)
