from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class RestApi(Resource):

    def get(self):
        return {'board': list(self.game.board)}

api.add_resource(RestApi, '/')

app.run(debug=True)