from flask import Flask
from flask_restful import Resource, Api, reqparse
from BOILERPLATERouter import BOILERPLATE

app = Flask(__name__)

api = Api(app)



@app.route('/')
def index():
    return {'message': 'Boilerplate'}, 200


class BOILERPLATE2(Resource):
    def get(self, id):
        print(id)
        return {'message':id, 'number':2}


class BOILERPLATE3(Resource):
    def get(self, id):
        print(id)
        return {'message':id, 'number':3}




api.add_resource(BOILERPLATE, '/boilerplate')
api.add_resource(BOILERPLATE2, '/boilerplate/<int:id>')
api.add_resource(BOILERPLATE3, '/boilerplate/<string:id>')


if __name__ == "__main__":
    app.run(debug=True)