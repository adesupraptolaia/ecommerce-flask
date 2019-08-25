from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints.client.model import Clients
from blueprints.admin.model import Admins
from flask_cors import CORS

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

# Resources


class CreateTokenResources(Resource):

    def options(self):
        return {"status": "ok"}, 200

    def post(self):
        # Create token
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            location='json', required=True)
        parser.add_argument('password',
                            location='json', required=True)
        args = parser.parse_args()

        qry = Clients.query

        qry = qry.filter_by(username=args['username'])
        qry = qry.filter_by(password=args['password']).first()

        if qry is not None:
            client_data = marshal(qry, Clients.response_fields_jwt)
            token = create_access_token(
                identity=args['username'], user_claims=client_data)
        else:
            return {'status': 'UNATHORIZED', 'message': 'invalid username or password'}, 401
        return {'token': token}, 200


class CreateTokenAdminResources(Resource):
    def options(self):
        return {"status": "oke"}

    def post(self):
        # Create token
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        args = parser.parse_args()

        qry = Admins.query

        qry = qry.filter_by(username=args['username'])
        qry = qry.filter_by(email=args['email'])
        qry = qry.filter_by(password=args['password']).first()

        if qry is not None:
            admin_data = marshal(qry, Admins.response_fields)
            token = create_access_token(
                identity=args['username'], user_claims=admin_data)
        else:
            return {'status': 'UNATHORIZED', 'message': 'invalid username or password or email'}, 401
        return {'token': token}, 200

api.add_resource(CreateTokenResources, '')
api.add_resource(CreateTokenAdminResources, '/admin')