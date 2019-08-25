from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from .model import Transaction_detail
from sqlalchemy import desc
from blueprints import app, db, internal_required, non_internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims
from datetime import datetime


bp_transaction_detail = Blueprint('transaction_detail', __name__)
api = Api(bp_transaction_detail)


class TransactionDetailResource(Resource):

    def __init__(self):
        pass
    
    def options(self, id=None):
        return {"status": "oke"}

    @jwt_required
    @non_internal_required
    def get(self, id):  # get by id
        qry = Transaction_detail.query.get(id)
        if qry is not None:
            return marshal(qry, Transaction_detail.response_fields), 200, {'Content-Type': 'application/json'}
        return {'status': 'transaction_detail Not Found'}, 404, {'Content-Type': 'application/json'}


class TransactionDetailList(Resource):

    def __init__(self):
        pass

    def options(self):
        return {"status": "oke"}
        
    @jwt_required
    @non_internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('product_id', type=int, location='args')
        parser.add_argument('transaction_id', type=int, location='args')
        data = parser.parse_args()

        offset = (data['p'] * data['rp']) - data['rp']

        claims = get_jwt_claims()
        qry = Transaction_detail.query
        qry = qry.filter_by(client_id=claims['id'])

        
        if data['product_id'] is not None:
            qry = qry.filter_by(product_id=data['product_id'])

        if data['transaction_id'] is not None:
            qry = qry.filter_by(transaction_id=data['transaction_id'])

        rows = []
        for row in qry.limit(data['rp']).offset(offset).all():
            rows.append(marshal(row, Transaction_detail.response_fields))
        return rows, 200, {'Content-Type': 'application/json'}


api.add_resource(TransactionDetailList, '')
api.add_resource(TransactionDetailResource, '', '/<id>')
