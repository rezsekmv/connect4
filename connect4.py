from minmax import *

import time

def draw(win, game, p1, p2):
    game.draw(win, p1, p2)

    pygame.display.update()


def get_colnum(game):
    col = None
    while col is None or not col.isnumeric() or int(col)-1 < 0 or game.COLNUM <= int(col)-1:
        col = input("Player1: ")
    return int(col)


def main():

    # init
    pygame.init()
    game_over = False

    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Connect4")
    window.fill(BACKGROUND)

    game = Game()
    p1 = Player(1, RED)
    p2 = MinMaxPlayer(2, YELLOW)
    next_player = 1

    draw(window, game, p1, p2)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                quit()
                break

        if next_player == p1.id:
            col = get_colnum(game)

            placed = p1.move(col-1, game)

            if placed:
                next_player = p2.id

        elif next_player == p2.id:
            placed = p2.best_move(game, p1)

            if placed:
                next_player = p1.id


        win = game.isFinished()

        if win == 0:
            print("DRAW")
        elif win == p1.id:
            print("P1 WON")
        elif win == p2.id:
            print("P2 WON")

        draw(window, game, p1, p2)

    time.sleep(1)

main()