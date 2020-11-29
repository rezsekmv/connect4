import os
import pickle
import neat

from logic.player import *

def load_genome(id, game, genome_path="winner.pickle"):
    local_dir = os.path.dirname(__file__)
    config_file = os.path.join(local_dir, 'neat-config.txt')


    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    with open(genome_path, "rb") as f:
        genome = pickle.load(f)

    move(genome, config, id, game)


def move(genome, config, next_p, game):
    ai = Player(next_p)
    network = neat.nn.FeedForwardNetwork.create(genome, config)

    input_nodes = tuple(game.board.reshape(1, -1)[0])
    output_nodes = network.activate(input_nodes)
    # set output neurons and MOVE
    placed = False
    while not placed:
        best_column = output_nodes.index(max(output_nodes))
        placed = ai.move(best_column, game)
        output_nodes[best_column] = -2
