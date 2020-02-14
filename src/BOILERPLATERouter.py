from flask_restful import Resource, Api, reqparse

class BOILERPLATE(Resource):
    def get(self):

        return {'message':'gotm'}, 200


    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('boilerplate', required=True, type=str)

        args = parser.parse_args()

        print(args)
        return {'message':'Boilerplate', 'data':args}, 201

    
    def delete(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)

        args = parser.parse_args()

        return {}, 204