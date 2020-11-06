from player import *
from game import *
from logger import *

import random
import math


# =================================
# This is the class for the MiniMax algorithym
# =================================
class MinMaxPlayer(Player):

    def __init__(self, id, color=None):
        super().__init__(id, color)
        self.color = color
        self.depth = 6

    #=================================
    # place a circle on the board
    #=================================
    def move(self, column, game):
        return game.place(self, column)

    # =================================
    # Checks if the game is over
    # =================================
    def is_terminal_node(self, game):
        return game.isFinished()

    # =================================
    # Arrange columns (BEST columns first)
    # =================================
    def loop_order(self, game):
        columns = [i for i in range(game.COLNUM)]
        f = [abs(x-(game.COLNUM//2)) for x in range(game.COLNUM)]

        _, order = zip(*sorted(zip(f, columns)))
        return list(order)



    #=================================
    # The recursive minimax algorithym
    #=================================
    def minimax(self, game, rival, depth, alpha, beta, maximizing_player):

        # if the game is finished
        end = self.is_terminal_node(game)
        if end >= 0:
            if end == self.id:
                return 1000000000, None
            elif end == rival.id:
                return -100000000, None
            elif end == 0:
                return 0, None

        # reached the bottom of the tree
        if depth == 0:
            return self.board_score(game, rival), None

        # maximizing player (AI)
        if maximizing_player:
            score = -math.inf
            column = random.randint(0, 6)
            for col in self.loop_order(game):
                new_game = Game()
                new_game.board = game.board.copy()
                new_score = 0
                if new_game.place(self, col):
                    new_score, c = self.minimax(new_game, rival, depth-1, alpha, beta, False)
                    new_score += self.position_score(col)
                    if new_score > score:
                        score = new_score
                        column = col
                    # a-b phruning
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break

                if depth == self.depth:
                    LOGGER.info("MAX: col: {} score: {}".format( col+1, new_score))
            return score, column
        # minimizing player (the other player)
        else:
            score = math.inf
            column = random.randint(0,6)
            for col in self.loop_order(game):
                new_game = Game()
                new_game.board = game.board.copy()
                if new_game.place(rival, col):
                    new_score, c = self.minimax(new_game, rival, depth-1, alpha, beta, True)
                    new_score -= self.position_score(col)
                    if new_score < score:
                        score = new_score
                        column = col
                    # a-b phruning
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return score, column


    #=================================
    # get a score of a block of 4
    #=================================
    def block_score(self, block, rival):
        score = 0

        if block.count(rival.id) == 3 and block.count(0) == 1:
            score -= 300

        elif block.count(self.id) == 3 and block.count(0) == 1:
            score += 20

        elif block.count(self.id) == 2 and block.count(0) == 2:
            score += 6

        return score


    #=================================
    # get the score of the full board
    #=================================
    def board_score(self, game, rival):

        score = 0

        # horisontal
        for r in range(game.ROWNUM):
            for c in range(game.COLNUM - 3):
                block = list(game.board[r, c:c + 4])
                score += self.block_score(block, rival)

        # vertical
        for c in range(game.COLNUM):
            for r in range(game.ROWNUM - 3):
                block = list(game.board[r:r + 4, c])
                score += self.block_score(block, rival)

        # diagonal
        for r in reversed(range(3, game.ROWNUM)):
            for c in range(game.COLNUM - 3):
                block = [game.board[r - i, c + i] for i in range(4)]
                score += self.block_score(block, rival)

        for r in reversed(range(3, game.ROWNUM)):
            for c in reversed(range(3, game.COLNUM)):
                block = [game.board[r - i, c - i] for i in range(4)]
                score += self.block_score(block, rival)

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
    def best_move(self, game, rival):

        '''if game.board.tolist().count(0) == 42-13:
            self.depth = 9

        if game.board.tolist().count(0) == 42-15:
            self.depth = 30'''

        score, column = self.minimax(game, rival, self.depth, -math.inf, math.inf, True)
        LOGGER.info("CHOOSEN: col: {} score: {}".format(column + 1, score))
        LOGGER.info("-" * 30)
        return self.move(column, game)
