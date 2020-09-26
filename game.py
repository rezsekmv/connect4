from constants import *

import pygame
import numpy

class Game:

    def __init__(self):
        self.ROWNUM = 6
        self.COLNUM = 7
        self.board = numpy.zeros((self.ROWNUM, self.COLNUM))
        self.rect = (50, 150, 700, 600)
        self.radius = 30


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
    def isFinished(self, player):
        # row
        for row in range(self.ROWNUM - 3):
            for col in range(self.COLNUM):
                if self.board[row, col] == player.id and self.board[row + 1, col] == player.id and self.board[
                    row + 2, col] == player.id and self.board[row + 3, col] == player.id:
                    return True
        # col
        for row in range(self.ROWNUM):
            for col in range(self.COLNUM - 3):
                if self.board[row, col] == player.id and self.board[row, col + 1] == player.id and self.board[
                    row, col + 2] == player.id and self.board[row, col + 3] == player.id:
                    return True

        # diag
        for row in range(self.ROWNUM - 3):
            for col in range(self.COLNUM - 3):
                if self.board[row, col] == player.id and self.board[row + 1, col + 1] == player.id and self.board[
                    row + 2, col + 2] == player.id and self.board[row + 3, col + 3] == player.id:
                    return True

        for row in range(self.ROWNUM - 3):
            for col in reversed(range(3, self.COLNUM)):
                if self.board[row, col] == player.id and self.board[row + 1, col - 1] == player.id and self.board[
                    row + 2, col - 2] == player.id and self.board[row + 3, col - 3] == player.id:
                    return True

        return False


    #=================================
    # draws the entire game
    #=================================
    def draw(self, win, p1, p2):
        pygame.draw.rect(win, BLUE, self.rect)
        x_gap = int(self.rect[2] / (self.COLNUM + 1))
        y_gap = int(self.rect[3] / (self.ROWNUM + 1))

        for i in range(self.COLNUM):
            for j in range(self.ROWNUM):
                item = self.board[j, i]

                if item == 0:
                    pygame.draw.circle(win, GREY, (self.rect[0] + (i + 1) * x_gap, self.rect[1] + (j + 1) * y_gap),
                                       self.radius)
                elif item == p1.id:
                    p1.draw(win, (self.rect[0] + (i + 1) * x_gap, self.rect[1] + (j + 1) * y_gap), self.radius )

                elif item == p2.id:
                    p2.draw(win, (self.rect[0] + (i + 1) * x_gap, self.rect[1] + (j + 1) * y_gap), self.radius )

