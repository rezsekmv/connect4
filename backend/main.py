from restapi import *
from minmax import *

def get_colnum(game):
    col = None
    while col is None or not col.isnumeric() or int(col)-1 < 0 or game.COLNUM <= int(col)-1:
        col = input("Player1: ")
    return int(col)


def main():

    # init
    game_over = False
    game = Game()
    p1 = Player(1, RED)
    p2 = MinMaxPlayer(2, YELLOW)
    next_player = p1
    rival = p2

    app, api = init_api()
    add_resources(api)
    run_api(app)


'''
        placed = False
        if type(next_player) is MinMaxPlayer:
            placed = next_player.best_move(game, rival)
        elif type(next_player) is Player:
            col = get_colnum(game)
            placed = next_player.move(col-1, game)

        if placed:
            if next_player == p1:
                next_player = p2
                rival = p1
            elif next_player == p2:
                next_player = p1
                rival = p2

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
        '''

main()
