from restapi import *

def main():

    app, api = init_api()
    add_resources(api)
    run_api(app)

def replay_genome(config_file, genome_path="winner.pickle"):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    with open(genome_path, "rb") as f:
        genome = pickle.load(f)

    play_against_human(genome, config, 2)

def main():
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neat-config.txt')
    replay_genome(config_path)

main()
