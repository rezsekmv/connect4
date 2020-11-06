import copy

from constants import *
from draw import *
from minmax import *
from game import *
from logger import *

import neat

def check_win(i, ai, opponent, fitness, game_list, genome_list):
    # check for win and fill genome fitnesses
    win = game_list[i].isFinished()
    if win == 0:
        # if draw fitness is 50
        genome_list[i].fitness = 50
        LOGGER.info("DRAW")
    elif win == opponent.id:
        genome_list[i].fitness = fitness
        LOGGER.info("OPPONENT WON")
    elif win == ai.id:
        genome_list[i].fitness = 100 - fitness
        LOGGER.info("AI WON")

    return not win == -1


def eval_genomes(genomes, config):
    network_list = []
    player_list = []
    genome_list = []

    game_list = []
    fitness = 0

    # init
    opponent = MinMaxPlayer(2, YELLOW)

    for _, genome in genomes:
        genome.fitness = 0
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        network_list.append(network)
        player_list.append(Player(1, RED))
        genome_list.append(genome)

        game_list.append(Game())


    while len(player_list) > 0:
        fitness += 1
        for i, ai in enumerate(player_list):

            # 2nd try input = tuple(map(tuple, game.board))
            input_nodes = tuple(game_list[i].board.reshape(1, -1)[0])
            output_nodes = network_list[player_list.index(ai)].activate(input_nodes)

            # set output neurons and MOVE
            placed = False
            while not placed:
                best_column = output_nodes.index(max(output_nodes))
                placed = ai.move(best_column, game_list[i])
                output_nodes[best_column] = -2

        i = 0
        while i < len(player_list):
            if check_win(i, player_list[i], opponent, fitness, game_list, genome_list):
                player_list.pop(i)
                network_list.pop(i)
                genome_list.pop(i)
                game_list.pop(i)
                i -= 1
            i += 1

        for i in range(len(player_list)):
            # other player move
            opponent.best_move(game_list[i], player_list[i])

        i = 0
        while i < len(player_list):
            if check_win(i, player_list[i], opponent, fitness, game_list, genome_list):
                player_list.pop(i)
                network_list.pop(i)
                genome_list.pop(i)
                game_list.pop(i)
                i -= 1
            i += 1

        if len(player_list)>0:
            for i in range(len(player_list)):
                draw_game(window, game_list[i], player_list[i], opponent)
                pygame.time.delay(2000)
