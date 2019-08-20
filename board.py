class Board:
    def __init__(self, height, width):
        """constructs new board object"""
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """returns string representing board"""
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += '-' * self.width*2 + '\n'
        count = 0
        while count != self.width:
            s += ' ' + str(count)
            count += 1
        return s

    def add_checker(self, checker, col):
        """adds a checker to the board"""
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = self.height - 1
        while self.slots[row][col] != ' ':
            row -= 1
        if self.slots[row][col] == ' ':
            self.slots[row][col] = checker


    def reset(self):
        """resets entire board"""
        self.__init__(self.height, self.width)

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """returns true if can place checker in col"""
        if col < 0 or col >= self.width or self.slots[0][col] != ' ':
            return False
        else:
            return True

    def is_full(self):
        """returns whether the board is completely full"""
        for x in range(self.width):
            if self.slots[0][x] == ' ':
                return False
        return True

    def remove_checker(self, col):
        """removes top checker from col"""
        for x in range(self.height):
            if self.slots[x][col] != ' ':
                self.slots[x][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
    """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """checks for vertical win"""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                        return True
        return False

    def is_down_diagonal_win(self, checker):
        """diagonal down from left to right"""
        for row in range(0, self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                        return True
        return False

    def is_up_diagonal_win(self, checker):
        """is down diagonal from left to right"""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                        return True
        return False
                
    def is_win_for(self, checker):
        """returns whether there are four in a row for checker"""
        assert(checker == 'X' or checker == 'O')
        return self.is_horizontal_win(checker) or self.is_vertical_win(checker) or self.is_down_diagonal_win(checker) or self.is_up_diagonal_win(checker)
        
