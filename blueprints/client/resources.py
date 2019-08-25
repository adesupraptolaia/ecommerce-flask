from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from .model import Clients
from ..client_detail.model import ClientDetails
from sqlalchemy import desc
from blueprints import app, db, internal_required, non_internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_client = Blueprint('client', __name__)
api = Api(bp_client)


class ClientResource(Resource):

    def __init__(self):
        pass

    def options(self):
        return {"status": "oke"}

    # hanya bisa melihat akunnya sendiri
    @jwt_required
    @non_internal_required
    def get(self): 
        claims = get_jwt_claims()
        qry = Clients.query.get(claims['id'])
        if qry is not None:
            return marshal(qry, Clients.response_fields_jwt), 200, {'Content-Type': 'application/json'}
        return {'status': 'Client Not Found'}, 404, {'Content-Type': 'application/json'}

    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
       
        # CLIENT ADALAH PEMBELI, JADI STATUS = 0 / FALSE
       
        data = parser.parse_args()
        
        client_qry = Clients.query.filter_by(username=data['username']).first()
        if client_qry is not None:
            return {'status': 'please input another username'}
            
        client = Clients(data['username'], data['password'], data['email'])
        db.session.add(client)
        db.session.commit()

        app.logger.debug('DEBUG : %s', client)

        return marshal(client, Clients.response_fields_jwt), 200, {'Content-Type': 'application/json'}

    @jwt_required
    @non_internal_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
       
        # CLIENT ADALAH PEMBELI, JADI STATUS = 0 / FALSE
        data = parser.parse_args()

        claims = get_jwt_claims()
        qry = Clients.query.get(claims['id'])

        qry.username = data['username']
        qry.password = data['password']
        qry.email = data['email']
        
        db.session.commit()

        app.logger.debug('DEBUG : %s', qry)

        return marshal(qry, Clients.response_fields_client_detail), 200, {'Content-Type': 'application/json'}

    # @jwt_required
    # @non_internal_required
    # def delete(self):
    #     claims = get_jwt_claims()

    #     qry = Clients.query.get(claims['id'])
    #     if qry is None:
    #         return {'status': 'Client Not Found'}, 404, {'Content-Type': 'application/json'}

    #     db.session.delete(qry)
    #     db.session.commit()

    #     return {'status': 'Client Deleted'}, 200, {'Content-Type': 'application/json'}
   
api.add_resource(ClientResource, '')
