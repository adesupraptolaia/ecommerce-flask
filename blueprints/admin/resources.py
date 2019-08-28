from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from .model import Admins
from sqlalchemy import desc
from blueprints import app, db, internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims


bp_admin = Blueprint('admin', __name__)
api = Api(bp_admin)


class AdminResource(Resource):

    def __init__(self):
        pass

    @jwt_required
    @internal_required
    def get(self):
        claims = get_jwt_claims()

        # just one admin, admin = pemilik toko
        qry = Admins.query.get(claims["id"])
        return marshal(qry, Admins.response_fields), 200, {'Content-Type': 'application/json'}

    @jwt_required
    @internal_required
    def put(self):
        claims = get_jwt_claims()

        # if admin want to change the data
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        data = parser.parse_args()

        qry = Admins.query.get(claims['id'])

        if qry is None:
            return {'status': 'USER_NOT_FOUND'}, 404

        qry.username = data['username']
        qry.password = data['password']
        qry.email = data['email']

        db.session.commit()

        return marshal(qry, Admins.response_fields), 200, {'Content-Type': 'application/json'}

    def options(self):
        return {"status": "oke"}, 200


api.add_resource(AdminResource, '')
