from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from minmax import *

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

class Move(Resource):

    # curl -H "Content-Type: application/json" -X POST -d '@data.json'  http://localhost:5000/move
    def post(self):
        # request
        json = request.get_json()
        game = json_to_game(json["board"])
        p1_type = json["player1"]
        p2_type = json["player2"]
        next_player = json['next_player']
        wonBy = game.isFinished()

        if wonBy > 0:
            return {
                'board': game_to_json(game),
                'wonBy': wonBy
            }

        if next_player == 1:
            if p1_type == 'minmax':
                p1 = MinMaxPlayer(1)
                p2 = Player(2)
                p1.best_move(game, p2)
                wonBy = game.isFinished()
                return {
                    'board': game_to_json(game),
                    'next_player': 2,
                    'wonBy': wonBy
                }
        elif next_player == 2:
            if p2_type == 'minmax':
                p1 = Player(1)
                p2 = MinMaxPlayer(2)
                p2.best_move(game, p1)
                wonBy = game.isFinished()
                return {
                    'board': game_to_json(game),
                    'next_player': 1,
                    'wonBy': wonBy
                }

        # response
        return {
            'board': game_to_json(game),
            'next_player': 0,
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
    api.add_resource(Move, '/move')


def run_api(app):
    app.run(debug=True, host='152.66.239.241') #