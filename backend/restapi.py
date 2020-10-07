from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

from minmax import *

def init_api():
    app = Flask(__name__)
    cors = CORS(app)
    #app.config['CORS_HEADERS'] = 'Content-Type'
    api = Api(app)
    return app, api

class RestApi(Resource):

    # curl http://localhost:5000/
    def get(self):
        return {'get': 'req'}

    # curl -H "Content-Type: application/json" -X POST -d '@data.json'  http://localhost:5000/
    def post(self):
        # request
        json = request.get_json()
        game = self.json_to_game(json["board"])
        rival = Player(json["human"])
        ai = MinMaxPlayer(json["ai"])

        # calculate
        ai.best_move(game, rival)

        # response
        return {
            'board': self.game_to_json(game),
            'ai': True
        }

    def json_to_game(self, board):
        game = Game()
        game.board = numpy.array(board)
        return game

    def game_to_json(self, game):
        return game.board.tolist()


def add_resources(api):
    api.add_resource(RestApi, '/move')

def run_api(app):
    app.run(debug=True)