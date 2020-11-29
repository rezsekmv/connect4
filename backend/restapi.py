from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from logic.minmax import *
from logic.neatai import *


def init_api():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    return app, api

def json_to_game(board):
    game = Game()
    game.board = numpy.array(board)
    return game

def game_to_json(game):
    return game.board.tolist()

def calc_other_player(id):
    return (id  % 2) +1

class MinMax(Resource):

    # curl -H "Content-Type: application/json" -X POST -d '@data.json'  http://localhost:5000/move
    def post(self):
        # request
        json = request.get_json()
        game = json_to_game(json["board"])
        next_player_id = json['next_player']

        minmax = MinMaxPlayer(next_player_id)
        rival = Player(calc_other_player(next_player_id))
        minmax.best_move(game, rival)

        wonBy = game.isFinished()
        return {
            'board': game_to_json(game),
            'next_player': calc_other_player(next_player_id),
            'wonBy': wonBy
        }

        # response

class NeatAi(Resource):
    def post(self):
        json = request.get_json()
        game = json_to_game(json["board"])

        next_player_id = json["next_player"]

        load_genome(next_player_id, game)

        wonBy = game.isFinished()
        if wonBy > 0:
            return {
                'board': game_to_json(game),
                'wonBy': wonBy
            }

        # response
        return {
            'board': game_to_json(game),
            'next_player': calc_other_player(next_player_id),
            'wonBy': wonBy,
        }

class CheckWin(Resource):

    def post(self):
        json = request.get_json()
        game = json_to_game(json["board"])
        wonBy = game.isFinished()
        return {
            'wonBy': wonBy
        }

def add_resources(api):
    api.add_resource(CheckWin, '/checkwin')
    api.add_resource(MinMax, '/minmax')
    api.add_resource(NeatAi, '/neatai')


def run_api(app):
    app.run(debug=True, host='192.169.1.9')
