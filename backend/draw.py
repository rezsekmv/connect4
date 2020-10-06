from constants import *

import pygame

# =================================
# pygame init
# =================================
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Connect4")
window.fill(BLACK)
pygame.draw.rect(window, BLUE, (50, 150, 200, 500))

# =================================
# draws the entire game
# =================================
def draw_game(win, game, p1, p2):
    rect = (50, 150, 700, 600)
    radius = 30

    pygame.draw.rect(win, BLUE, game.rect)
    x_gap = int(game.rect[2] / (game.COLNUM + 1))
    y_gap = int(game.rect[3] / (game.ROWNUM + 1))

    for i in range(game.COLNUM):
        for j in range(game.ROWNUM):
            item = game.board[j, i]

            if item == 0:
                pygame.draw.circle(win, GREY, (rect[0] + (i + 1) * x_gap, rect[1] + (j + 1) * y_gap), radius)
            elif item == p1.id:
                draw_player(p1, win, (rect[0] + (i + 1) * x_gap, rect[1] + (j + 1) * y_gap), radius)

            elif item == p2.id:
                draw_player(p2, win, (rect[0] + (i + 1) * x_gap, rect[1] + (j + 1) * y_gap), radius)

    pygame.display.update()

#=================================
# draws a player
#=================================
def draw_player(player, win, coords, r):
    pygame.draw.circle(win, player.color, coords, r)
