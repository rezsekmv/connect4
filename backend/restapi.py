from flask import Flask, request
from flask_restful import Api, Resource

def init_api():
    app = Flask(__name__)
    api = Api(app)
    return app, api

class RestApi(Resource):

    def __init__(self):
        self.game = 1

    def get(self):
        self.game += 1
        return {'board': self.game}

    def post(self):
        json = request.get_json()
        json.key1 += 1
        return json, 201

def add_resources(api):
    api.add_resource(RestApi, '/')

def run_api(app):
    app.run(debug=True)