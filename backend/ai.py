
from constants import *
# from draw import *
from player import *
from game import *
from logger import *

import neat

def check_win(game, fitness, genome_list):
    # check for win and fill genome fitnesses
    win = game.isFinished()
    if win == 0:
        # if draw fitness is 50
        genome_list[game.player1].fitness = 50
        genome_list[game.player2].fitness = 50
        LOGGER.info("DRAW")
    elif win == game.next_player.id:
        if game.next_player.id == 1:
            genome_list[game.player1].fitness = 100 - fitness
            genome_list[game.player2].fitness = fitness
        if game.next_player.id == 2:
            genome_list[game.player2].fitness = 100 - fitness
            genome_list[game.player1].fitness = fitness
        LOGGER.info("Game won by" + str(game.next_player.id))

    return not win == -1


def eval_genomes(genomes, config):
    genome_list = []
    network_list = []
    game_list = []

    fitness = 0

    for _, genome in genomes:
        genome.fitness = 0
        network = neat.nn.FeedForwardNetwork.create(genome, config)

        genome_list.append(genome)
        network_list.append(network)

    red1 = Player(1, RED)
    yellow2 = Player(2, YELLOW)

    length = len(genomes)
    for i in range(length):
        for j in range(length):
            if i != j:
                p1 = i
                p2 = j
                game_list.append(Game(p1, p2, red1))

    while len(game_list) > 0:
        # increase fitness
        fitness += 1

        # AI move
        for game in game_list:

            # 2nd try input = tuple(map(tuple, game.board))
            input_nodes = tuple(game.board.reshape(1, -1)[0])
            output_nodes = [0,0,0,0,0,0,0]
            if game.next_player == red1:
                output_nodes = network_list[game.player1].activate(input_nodes)
            if game.next_player == yellow2:
                output_nodes = network_list[game.player2].activate(input_nodes)

            # set output neurons and MOVE
            placed = False
            while not placed:
                best_column = output_nodes.index(max(output_nodes))
                placed = game.next_player.move(best_column, game)
                output_nodes[best_column] = -2

            # check for win and if the game is over take out from the list
            if check_win(game, fitness, genome_list):
                game_list.remove(game)

        if game.next_player == red1:
            game.next_player = yellow2
        if game.next_player == yellow2:
            game.next_player = red1


        # if len(player_list)>0:
        #     for i in range(len(player_list)):
        #         draw_game(window, game_list[i], player_list[i], opponent)
        #         pygame.time.delay(2000)
