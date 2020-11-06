import numpy

class Game:

    def __init__(self, p1, p2, next_p = 1):
        self.ROWNUM = 6
        self.COLNUM = 7
        self.board = numpy.zeros((self.ROWNUM, self.COLNUM))
        self.player1 = p1
        self.player2 = p2
        self.next_player = next_p

    def __str__(self):
        return str(self.board)

    #=================================
    # place a players circle
    #=================================
    def place(self, player, column):
        for i in reversed(range(self.ROWNUM)):
            if self.board[i, column] == 0:
                self.board[i, column] = player.id
                return True
        return False

    #=================================
    # checks if the game is over
    #=================================
    def isFinished(self):

        if not 0 in self.board:
            return 0

        for id in range(1,3):
            # row
            for row in range(self.ROWNUM - 3):
                for col in range(self.COLNUM):
                    if self.board[row, col] == id and self.board[row + 1, col] == id and self.board[
                        row + 2, col] == id and self.board[row + 3, col] == id:
                        return id
            # col
            for row in range(self.ROWNUM):
                for col in range(self.COLNUM - 3):
                    if self.board[row, col] == id and self.board[row, col + 1] == id and self.board[
                        row, col + 2] == id and self.board[row, col + 3] == id:
                        return id

            # diag
            for row in range(self.ROWNUM - 3):
                for col in range(self.COLNUM - 3):
                    if self.board[row, col] == id and self.board[row + 1, col + 1] == id and self.board[
                        row + 2, col + 2] == id and self.board[row + 3, col + 3] == id:
                        return id

            for row in range(self.ROWNUM - 3):
                for col in reversed(range(3, self.COLNUM)):
                    if self.board[row, col] == id and self.board[row + 1, col - 1] == id and self.board[
                        row + 2, col - 2] == id and self.board[row + 3, col - 3] == id:
                        return id

        return -1

