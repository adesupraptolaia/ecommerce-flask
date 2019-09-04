from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from .model import ClientDetails
from sqlalchemy import desc
from blueprints import app, db, internal_required, non_internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_client_detail = Blueprint('client_detail', __name__)
api = Api(bp_client_detail)


class ClientDetailsResource(Resource):

    def options(self):
        return {"status": "oke"}, 200

    def __init__(self):
        pass

    @jwt_required
    @non_internal_required
    def get(self):
        claims = get_jwt_claims()
        qry = ClientDetails.query.get(claims['id'])
        if qry is not None:
            return marshal(qry, ClientDetails.response_fields), 200, {'Content-Type': 'application/json'}
        return {'status': 'Client detail Not Found'}, 404, {'Content-Type': 'application/json'}

    @jwt_required
    @non_internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fullname', location='json', required=True)
        parser.add_argument('phone', location='json', required=True)
        parser.add_argument('address', location='json', required=True)
        
        data = parser.parse_args()
        claims = get_jwt_claims()

        qry = ClientDetails.query.get(claims['id'])        
        if qry is not None:
            return {'status': 'Client detail cannot be posted again'}, 404, {'Content-Type': 'application/json'}

        client_details = ClientDetails(claims['id'], data['fullname'], data['phone'], data['address'])
        db.session.add(client_details)
        db.session.commit()

        app.logger.debug('DEBUG : %s', client_details)

        return marshal(client_details, ClientDetails.response_fields), 200, {'Content-Type': 'application/json'}

    @jwt_required
    @non_internal_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fullname', location='json', required=True)
        parser.add_argument('phone', location='json', required=True)
        parser.add_argument('address', location='json', required=True)
        data = parser.parse_args()

        claims = get_jwt_claims()
        qry = ClientDetails.query.get(claims['id'])

        if qry is None:
            return {'status': 'Client detail Not Found'}, 404, {'Content-Type': 'application/json'}

        qry.fullname = data['fullname']
        qry.phone = data['phone']
        qry.address = data['address']
        db.session.commit()

        return marshal(qry, ClientDetails.response_fields), 200, {'Content-Type': 'application/json'}


api.add_resource(ClientDetailsResource, '')
