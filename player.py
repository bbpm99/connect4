#
# A Connect-Four Player class 
#  

from board import Board


class Player:
    def __init__(self, checker):
        """constructs new player with checker attribute and num of moves"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """returns string representing a player object"""
        return 'Player ' + self.checker

    def opponent_checker(self):
        """returns one-charcter stirng representing checker of opponent"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """accepts Board object and returns column where player wants to make move"""
        col = int(input('Enter a column: '))
        self.num_moves += 1
        while board.can_add_to(col) == False:
            print("Try again!")
            col = int(input('Enter a column: '))
        return col
