from player import *
from game import *

import random
import math

class Method:
   GAME_SCORE = 1
   COLUMN_SCORE = 2
   MINIMAX = 3


# =================================
# This is the class for the MiniMax algorithym
# =================================
class MinMaxPlayer(Player):

    def __init__(self, id, color):
        super().__init__(id, color)

    #=================================
    # place a circle on the board
    #=================================
    def move(self, column, game):
        return game.place(self, column)


    #=================================
    # The recursive minimax algorithym
    #=================================
    def minimax(self, game, depth, maximizing_player):

        if depth == 0:
            return self.board_score(game)

        if maximizing_player:
            score = -math.inf
            column = random.randint(0,6)
            for col in range(game.COLNUM):
                new_game = Game()
                new_game.board = game.board.copy()
                if new_game.place(self, col):
                    new_score = self.minimax(new_game, depth-1, False)
                    if new_score > score:
                        score = new_score
                        column = col
            return score
        else:
            score = math.inf
            column = random.randint(0,6)
            for col in range(game.COLNUM):
                new_game = Game()
                new_game.board = game.board.copy()
                if new_game.place(self, col):
                    new_score = self.minimax(new_game, depth-1, True)
                    if new_score < score:
                        score = new_score
                        column = col
            return score


    #=================================
    # get a score of a block of 4
    #=================================
    def block_score(self, block):
        score = 0
        if self.id == 1:
            rival = 2
        else:
            rival = 1

        if block.count(self.id) == 4:
            score += 1500

        elif block.count(rival) == 3 and block.count(0) == 1:
            score -= 300

        elif block.count(rival) == 2 and block.count(0) == 2:
            score -= 200

        elif block.count(self.id) == 3 and block.count(0) == 1:
            score += 20

        elif block.count(self.id) == 2 and block.count(0) == 2:
            score += 5

        return score


    #=================================
    # get the score of the full board
    #=================================
    def board_score(self, game):

        score = 0

        # horisontal
        for r in range(game.ROWNUM):
            for c in range(game.COLNUM - 3):
                block = list(game.board[r, c:c + 4])
                score += self.block_score(block)

        # vertical
        for c in range(game.COLNUM):
            for r in range(game.ROWNUM - 3):
                block = list(game.board[r:r + 4, c])
                score += self.block_score(block)

        # diagonal
        for r in reversed(range(3, game.ROWNUM)):
            for c in range(game.COLNUM - 3):
                block = [game.board[r - i, c + i] for i in range(4)]
                score += self.block_score(block)

        for r in reversed(range(3, game.ROWNUM)):
            for c in reversed(range(3, game.COLNUM)):
                block = [game.board[r - i, c - i] for i in range(4)]
                score += self.block_score(block)

        return score


    #=================================
    # get the score around a single circle
    #=================================
    def col_score(self, game, column):
        score = 0

        # which row is next in the column
        row = 0
        for r in range(game.ROWNUM):
            if game.board[r, column] != 0:
                row = r
                break

        # horisontal blocks
        for c in range(game.COLNUM - 3):
            if column >= c and column < c + 4:
                block = list(game.board[row, c:c + 4])
                score += self.block_score(block)

        # vertical blocks
        for r in range(game.ROWNUM - 3):
            if row >= r and row < r + 4:
                block = list(game.board[r:r + 4, column])
                score += self.block_score(block)

        # diagonal blocks
        for r in reversed(range(3, game.ROWNUM)):
            for c in range(game.COLNUM - 3):
                if (row == r and column == c) or (row == r - 1 and column == c + 1) or (
                        row == r - 2 and column == c + 2) or (row == r - 3 and column == c + 3):
                    block = [game.board[r - j][c + j] for j in range(4)]
                    score += self.block_score(block)

        for r in reversed(range(3, game.ROWNUM)):
            for c in range(3, game.COLNUM):
                if (row == r and column == c) or (row == r - 1 and column == c - 1) or (
                        row == r - 2 and column == c - 2) or (row == r - 3 and column == c - 3):
                    block = [game.board[r - j][c - j] for j in range(4)]
                    score += self.block_score(block)

        return score


    #=================================
    # score positional places more
    #=================================
    def position_score(self, col):
        # position scoring (more middle more points)
        return ((-abs(col - 3) + 4) + (-(col - 3) ** 2 + 4)) / 2


    #=================================
    # find the best move based on score
    #=================================
    def best_move(self, game, method):

        best_column = random.randrange(0, 6)
        best_score = -10000
        new_game = Game()

        for i in range(game.COLNUM):
            score = 0
            new_game.board = game.board.copy()
            if self.move(i, new_game):

                if method == Method.GAME_SCORE:
                    score = self.board_score(new_game)
                elif method == Method.COLUMN_SCORE:
                    score = self.col_score(new_game, i)
                elif method == Method.MINIMAX:
                    score = self.minimax(game, 3, True)

                score += self.position_score(i)

                # checking if it's a new best score / best column
                if best_score < score:
                    best_score = score
                    best_column = i

            print("col:", i + 1, "score:", score)

        return self.move(best_column, game)