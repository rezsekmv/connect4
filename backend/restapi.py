from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from game import *

def init_api():
    app = Flask(__name__)
    api = Api(app)
    return app, api

class RestApi(Resource):

    def get(self):
        return {'get': 'req'}

    # curl -H "Content-Type: application/json" -X POST -d '@data.json'  http://localhost:5000/
    def post(self):
        json = request.get_json()
        return json, 201

    def json_to_game(self, json):
        game = Game()
        game.board = json.board


def add_resources(api):
    api.add_resource(RestApi, '/asd')

def run_api(app):
    app.run(debug=True)