import copy

from draw import *
from minmax import *
from game import *

import neat


def eval_genomes(genomes, config):
    network_list = []
    player_list = []
    genome_list = []

    game_list = []
    fitness_list = []

    reward = 100

    # init
    opponent = MinMaxPlayer(1, RED)
    ai = Player(2, YELLOW)

    for _, genome in genomes:
        genome.fitness = 0
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        network_list.append(network)
        player_list.append(copy.copy(ai))
        genome_list.append(genome)

        game_list.append(Game())
        fitness_list.append(0)

    game_over = False
    while not game_over and len(player_list) > 0:

        for i, ai in enumerate(player_list):
            fitness_list[i] += 1

            # 2nd try input = tuple(map(tuple, game.board))
            input_nodes = tuple(game_list[i].board.reshape(1, -1)[0])
            output_nodes = network_list[player_list.index(ai)].activate(input_nodes)

            # set output neurons and MOVE
            placed = False
            while not placed:
                placed = ai.move(output_nodes.index(max(output_nodes)), game_list[i])
                output_nodes.remove(max(output_nodes))

            # other player move
            placed = False
            while not placed:
                placed = opponent.best_move(game_list[i], ai)

            #check for win and fill genome fitnesses
            win = game_list[i].isFinished()
            if win == 0:
                #if draw fitness is 50
                genome_list[i].fitness = 50
                print("DRAW")
                game_over = True
            elif win == opponent.id:
                genome_list[i].fitness = fitness_list[i]
                print("OPPONENT WON")
                game_over = True
            elif win == ai.id:
                genome_list[i].fitness = reward - fitness_list[i]
                print("AI WON")
                game_over = True

        # get best player
        best_index = fitness_list.index(max(fitness_list))

        #draw
        draw_game(window, game_list[best_index], opponent, ai)

        # break if score gets large enough
        '''if score > 20:
            pickle.dump(network_list[0],open("best.pickle", "wb"))
            break'''