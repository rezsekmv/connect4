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
    p1 = MinMaxPlayer(1, RED)
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
            placed = False

            if type(p1) is MinMaxPlayer:
                placed = p1.best_move(game, p1)
            if type(p1) is Player:
                col = get_colnum(game)
                placed = p1.move(col-1, game)

            if placed:
                next_player = p2.id

        elif next_player == p2.id:
            placed = False

            # order is neccesary cause p2 is always a Player
            if type(p2) is MinMaxPlayer:
                placed = p2.best_move(game, p2)
            elif type(p2) is Player:
                col = get_colnum(game)
                placed = p2.move(col-1, game)

            if placed:
                next_player = p1.id


        win = game.isFinished()

        if win == 0:
            print("DRAW")
            game_over = True
        elif win == p1.id:
            print("P1 WON")
            game_over = True
        elif win == p2.id:
            print("P2 WON")
            game_over = True

        draw(window, game, p1, p2)
        input("Enter for next move")

    time.sleep(3)

main()
