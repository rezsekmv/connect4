import pygame
import numpy
import random
import time
import enum


WIN_WIDTH = 800
WIN_HEIGHT = 800
BACKGROUND = (50, 50, 50)
    
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (40, 40, 255)
GREY = (150, 150, 150)

# Using enum class create enumerations
class Method(enum.Enum):
   GAME_SCORE = 1
   COLUMN_SCORE = 2
   MINMAX = 3

class Player:

    def __init__(self, id, color):
        self.id = id
        self.color = color

    def move(self, column, game):
        return game.place(self, column)

class Circle:
    
    def __init__(self, player):
        self.player = player
    
    def draw(self, window, pos, r):
        pygame.draw.circle(window, self.color, pos, r)

class Game:

    def __init__(self):
        self.ROWNUM = 6
        self.COLNUM = 7
        self.board = numpy.zeros((self.ROWNUM, self.COLNUM))
        self.rect = (50, 150, 700, 600)
        self.radius = 27
    
    def place(self, player, column):
        for i in reversed(range(self.ROWNUM)):
            if self.board[i, column] == 0:
                self.board[i, column] = player.id
                return True
        return False

    def isFinished(self, player):
        #row
        for row in range(self.ROWNUM-3):
            for col in range(self.COLNUM):
                if self.board[row, col] == player.id and self.board[row+1, col] == player.id and self.board[row+2, col] == player.id and self.board[row+3, col] == player.id:
                    return True
        #col
        for row in range(self.ROWNUM):
            for col in range(self.COLNUM-3):
                if self.board[row, col] == player.id and self.board[row, col+1] == player.id and self.board[row, col+2] == player.id and self.board[row, col+3] == player.id:
                    return True

        #diag
        for row in range(self.ROWNUM-3):
            for col in range(self.COLNUM-3):
                if self.board[row, col] == player.id and self.board[row+1, col+1] == player.id and self.board[row+2, col+2] == player.id and self.board[row+3, col+3] == player.id:
                    return True

        for row in range(self.ROWNUM-3):
            for col in reversed(range(3, self.COLNUM)):
                if self.board[row, col] == player.id and self.board[row+1, col-1] == player.id and self.board[row+2, col-2] == player.id and self.board[row+3, col-3] == player.id:
                    return True

        return False
    
    def draw(self, win, player1, AI):
        pygame.draw.rect(win, BLUE, self.rect)
        x_gap = int(self.rect[2] / (self.COLNUM+1))
        y_gap = int(self.rect[3] / (self.ROWNUM+1))


        for i in range(self.COLNUM):
            for j in range(self.ROWNUM):
                item = self.board[j,i]

                if item == 0:
                    pygame.draw.circle(win, GREY, (self.rect[0] + (i+1)*x_gap, self.rect[1] + (j+1)*y_gap), self.radius)
                elif item == 1:
                    pygame.draw.circle(win, player1.color, (self.rect[0] + (i+1)*x_gap, self.rect[1] + (j+1)*y_gap), self.radius)
                elif item == 2:
                    pygame.draw.circle(win, AI.color, (self.rect[0] + (i+1)*x_gap, self.rect[1] + (j+1)*y_gap), self.radius)

class AIPlayer(Player):

    def __init__(self, id, color):
       super().__init__(id, color)

    def move(self, column, game):
        return game.place(self, column)

    def block_score(self, block):
        score = 0
        if block.count(self.id) == 4:
            score += 5000

        elif block.count(self.id) == 3 and block.count(0) == 1:
            score += 15

        elif block.count(self.id) == 2 and block.count(0) == 2:
            score += 3

        return score


    def get_game_score(self, game, rival):
        score = 0
        #horisontal
        for r in range(game.ROWNUM):
            for c in range(game.COLNUM-3):
                block = list(game.board[r, c:c+4])
                score += self.block_score(block)

        #vertical
        for c in range(game.COLNUM):
            for r in range(game.ROWNUM-3):
                block = list(game.board[r:r+4, c])
                score += self.block_score(block)

        #diagonal
        for r in reversed(range(3, game.ROWNUM)):
            for c in range(game.COLNUM-3):
                block = [game.board[r-i, c+i] for i in range(4)]
                score += self.block_score(block)

        for r in reversed(range(3, game.ROWNUM)):
            for c in reversed(range(3, game.COLNUM)):
                block = [game.board[r-i, c-i] for i in range(4)]
                score += self.block_score(block)

        return score;

    def get_col_score(self, game, rival, column):
        score = 0
        row = 0
        for r in range(game.ROWNUM):
            if game.board[r, column] != 0:
                row = r
                break

        #position scoring
        if column == 3:
            score += 4
        if column == 2 or column == 4:
            score += 3
        if column == 1 or column == 5:
            score += 1

        #horisontal blocks
        for c in range(game.COLNUM-3):
            if column >= c and column < c+4:
                block = list(game.board[row, c:c+4])
                score += self.block_score(block)

        #vertical blocks
        for r in range(game.ROWNUM-3):
            if row >= r and row < r+4:
                block = list(game.board[r:r+4, column])
                score += self.block_score(block)

        #diagonal blocks
        for r in reversed(range(3, game.ROWNUM)):
            for c in range(game.COLNUM-3):
                if (row == r and column == c) or (row == r-1 and column == c+1) or (row == r-2 and column == c+2) or (row == r-3 and column == c+3) :
                    block = [game.board[r-j][c+j] for j in range(4)]
                    score += self.block_score(block)                

        for r in reversed(range(3, game.ROWNUM)):
            for c in range(3, game.COLNUM):
                if (row == r and column == c) or (row == r-1 and column == c-1) or (row == r-2 and column == c-2) or (row == r-3 and column == c-3) :
                    block = [game.board[r-j][c-j] for j in range(4)]
                    score += self.block_score(block)  

        return score


    def best_move(self, game, rival, method):

        best_column = random.randrange(0, 6)
        best_score = 0
        new_game = Game()
        for i in range(game.COLNUM):
            score = -1
            new_game.board = game.board.copy()
            if self.move(i, new_game):

                if method == Method.GAME_SCORE:
                    score = self.get_game_score(new_game, rival)
                elif method == Method.COLUMN_SCORE:
                    score = self.get_col_score(new_game, rival, i)
                elif method == Method.MINMAX:
                    pass

                if best_score<score:
                    best_score = score
                    best_column = i
            print("col:", i+1, "score:", score)

        self.move(best_column, game)


def draw(win, board, player1, AI):
    board.draw(win, player1, AI)

    pygame.display.update()

def main():
    pygame.init()
    game_over = False

    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Connect4")
    window.fill(BACKGROUND)

    game = Game()
    player1 = Player(1, RED)
    AI = AIPlayer(2, YELLOW)
    next_player = 1

    draw(window, game, player1, AI)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                quit()
                break

        if next_player == 1:
            col = 100
            while col-1 > game.COLNUM:
                col = input("Player1: ")
                if col.isnumeric():
                    col = int(col)
                else:
                    col = 100

            placed = player1.move(col-1, game)
            
            if game.isFinished(player1):
                print("Player1 won")
                next_player = 0
                game_over = True

            
            if placed:
                next_player = 2

        elif next_player == 2:
            #placed = AI.move(col+1, game)
            placed = True
            AI.best_move(game, player1, Method.GAME_SCORE)

            if game.isFinished(AI):
                print("AI won")
                next_player = 0
                game_over = True
            
            if placed:
                next_player = 1
            
        draw(window, game, player1, AI)

    time.sleep(1)

main()